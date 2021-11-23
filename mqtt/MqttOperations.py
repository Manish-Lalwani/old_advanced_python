#json implementation
import paho.mqtt.client as mqtt
from logger import Logger
import logging
import time
#import my_beautify as mb
import inspect
import psycopg2
import json
from datetime import datetime,timedelta
import xml.etree.ElementTree as et
from my_dicord import DiscordWebhook1
import websocket
import threading


details_flag =0

l1 = Logger(console_output_flag=1,filename='mqtt_client_log',stream_handler_level=logging.INFO,file_handler_level=logging.DEBUG)
log = l1.get_logger()
print(log.handlers,log.level)




ws = websocket.WebSocket()
ws.connect('ws://localhost:8000/ws/new_test_case')

def ping_send1():
        while True:
            ws.send(json.dumps({'value': 'ping'}))
            print("workiiiing")
            time.sleep(2)



# #need to use async but for know using threading
# async def ping_send():
#     while 1:
#         time.sleep(1)
#         ws.send(json.dumps({'value': 'Test case intructions to controller'}))
#         print("working")
# #end



class MqttClient:
    def __init__(self,broker,topic,client_name):
        #stack = inspect.stack()
        #mb.details(stack, details_flag)

        self.broker = broker
        self.topic = topic
        self.client_name = client_name
        self.message_list = []

        self.client = mqtt.Client(self.client_name)
        self.client.on_connect = self.on_connect
        self.client.on_disconnect = self.on_disconnect
        self.client.on_log = self.on_log
        self.client.on_message = self.on_message

    def on_connect(self,client, userdata, flags, rc):
        #stack = inspect.stack()
        #mb.details(stack, details_flag)
        log.info('-------------------------------------')
        log.info("Connected successfully to Broker: {} ".format(self.broker)) if rc == 0 else log.error("Bad connection to Broker: {}, RETURNED CODE: {}".format(self.broker, rc))
        log.info("Subscribed successfully to topic: {}".format(self.topic)) if client.subscribe(self.topic) else log.error("Error in subscription to topic: ", self.topic)

    def on_log(self,client, userdata, level, buf):
        #stack = inspect.stack()
        #mb.details(stack, details_flag)
        log.debug("CLIENT: {}, USERDATA: {}, LEVEL: {}, BUFFER: {}".format(client,userdata,level,buf))

    def on_disconnect(self,client, userdata, flags, rc=None):
        #stack = inspect.stack()
        #mb.details(stack, details_flag)
        log.info("RC COde: {}".format(rc))

    def on_message(self,client, userdata, msg):
        #stack = inspect.stack()
        #mb.details(stack, details_flag)
        log.info("Recieved messge is: {}".format(str(msg.payload.decode("utf-8"))))
        self.message_list.append(msg)

        #temp code will try to separate this
        test_case_id = self.temp_database_write(str(msg.payload.decode("utf-8")))
        log.info("Going for sleep for 10 sec")
        time.sleep(10)
        self.temp_message_ack(test_case_id)

        #trmp calling status_checker after wards it will on it own run on a separate thread: 02
        self.test_case_schedule_checker(test_case_id)
        #temp end:02
        log.info("Going for sleep for 10 sec")
        time.sleep(10)
        self.temp_res_publish(test_case_id)


    def get_client(self):
        return self.client


    def temp_database_write(self,message1):
        try:
            ##print("in temp database type of message",type(message1))
            root = et.fromstring(message1)
            conn_dict = {
                'host' :"localhost",
                'database': "TempMsgDB",
                'user': "postgres",
                'password': "griffyn" }

            #temp date afterwards it will get in message string
            current_time = datetime.now()
            schedule_time = current_time + timedelta(seconds = 45)

            conn = psycopg2.connect(host=conn_dict['host'],database=conn_dict['database'],user=conn_dict['user'],password=conn_dict['password'])
            log.info("Connection successful to Database: {} ".format(conn_dict['database']))
            cursor = conn.cursor()

            # insert query
            query = """INSERT INTO temp_test_case_table(test_case_id,cabinet_id,test_group_name,test_suite_name,test_case_name,meter_id,actions,schedule_time) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
            record = (
                root[2].text, #test_case_ud
                root[0].text, #cabinet_id
                root[1][1].text, #test_group_name
                root[1][0][0].text, #test_suite_name
                root[1][0][1][1].text, #test_case_name
                root[1][0][1][0].text, #meter_id
                root[1][0][1][2].text, #action
                schedule_time
                )

            cursor.execute(query, record)
            #message_id = cursor.fetchone()[0]
            conn.commit()
            log.info("Database Write Successful for TestCaseID:{} ".format(root[2].text))

            #discord code
            log.info("starting discord operations")
            dw1 = DiscordWebhook1()
            dw1.authenticate()
            dw1.set_embed_new_2()
            dw1.send()

            return root[2].text
        except Exception as e:
            #log.error("Message write failure to database")
            log.error(e)
            conn.close()

    def temp_message_ack(self,test_case_id):
        try:
            self.client_publish = mqtt.Client("test_case_publisher")
            self.client_publish.on_connect = self.on_connect
            self.client_publish.on_disconnect = self.on_disconnect
            self.client_publish.on_log = self.on_log
            #self.client_publish.on_message = self.on_message
            self.client_publish.connect(self.broker)
            self.client_publish.publish('SS/tcnack',"{}:rcv:true".format(test_case_id))
            log.info("Acknowledgement sent successfully for TestCaseID:{}".format(test_case_id))
        except Exception as e:
            log.error(e)

    def temp_res_publish(self,test_case_id):
        try:
            self.client_publish = mqtt.Client("result_publisher")
            self.client_publish.on_connect = self.on_connect
            self.client_publish.on_disconnect = self.on_disconnect
            self.client_publish.on_log = self.on_log
            # self.client_publish.on_message = self.on_message
            self.client_publish.connect(self.broker)
            self.client_publish.publish('SS/tcnres', "{}:pass".format(test_case_id))
            log.info("Result sent successfully for TestCaseID:{}".format(test_case_id))

        except Exception as e:
            log.error(e)

    #Test Case status related function
    def test_case_schedule_checker(self,test_case_id): #temp passing test_case_id afterwards will fetch from database
        """THIS FUNCTION WILL BE RUNNIG CONTINUOUSLY ON SEPARATE THREAD, PERFORM FOLLOWING WORK
        1.CONSTANTLY CHECK IN DATABASE FOR SCHEDULE OF TEST CASE (SORT BY TIME)
        2. CALL INSTRUCTOR FUNCTION ON SCHEDULE
        3. CALL STATUS UPDATER FOR CHANGING THE STATUS OF TEST CASE TO RUNNING
        """
        time.sleep(7)  # temp
        log.info("-------------------------------------")
        log.info("FROM HERE ONLY FUNCTIONS CALL ARE EXECUTED FOR DEMO PURPOSE NO OPERATIONS ARE BEING PERFORMED")
        log.info("TestCase:{} is scheduled for now".format(test_case_id))
        self.temp_controller_instructor(test_case_id)


    def  db_status_updater(self,test_case_id,status):
        """THIS FUNCTION WILL BE CALLED TO UPDATE/CHANGE THE STATUS OF TASK IN DATABASE

        """
        time.sleep(7)  # temp
        log.info("Successfully change status to {} for TestCase:{}".format(status,test_case_id))

    def temp_controller_instructor(self,test_case_id):
        """THIS FUNCTION WILL BE CALLED WHEN A TEST CASE IS SCHEDULED FOR RUN
            EVERY CALL WILL BE FOR A DIFFEREN TEST CASE AND WILL BE RUNNING ON SEPARATE THREAD
        1. Will fetch respective TestCase data from database
        2. Give Instruction to controller for starting the task
        3. Get ACKNOWLEDGMENT FROM controller
        3. WAIT FOR STATUS OF RUNNING TEST ONCE GOT RESULT FROM CONTRLLER WILL CALL db_status_updater FOR UPDATING THE DATABASE"""

        time.sleep(7) #temp
        log.info("Sending Instruction for running TestCase:{} using WebSocket".format(test_case_id))

        #websocket code

        ws.send(json.dumps({'value': 'Test case intructions to controller'}))
        controller_acknowledgement = 1
        if controller_acknowledgement ==1:
            status = 'RUNNING'
            time.sleep(7)  # temp
            log.info("Acknowledged by controller successfully, Hence changing the status as RUNNING in Database")
            self.db_status_updater(test_case_id= test_case_id,status =status)

        else:
            log.info("Error on controller side")
            self.db_status_updater(test_case_id=test_case_id, status='ERROR')

        #temp code this result will be given by controller
        time.sleep(7)
        controller_result =1

        if controller_result ==1:
            status = 'PASS'
            time.sleep(7)  # temp
            log.info("TestCase:{} execution completed successfully, Hence changing the status as {} in Database".format(test_case_id,status))
            self.db_status_updater(test_case_id= test_case_id,status =status)

        else:
            status = 'FAIL'
            log.info("TestCase:{} execution FAILED, Hence changing the status as {} in Database".format(
                test_case_id, status))
            self.db_status_updater(test_case_id=test_case_id, status=status)


if __name__ == "__main__":
    ping_start = threading.Thread(target=ping_send1)
    ping_start.start()

    print("Test In main")
    broker = '172.16.1.127'
    obj1 = MqttClient(broker = broker,topic = 'CAB0103UK003/tcn',client_name='test_case_subscriber')
    client = obj1.get_client()


    try:
        print("Connecting to Broker: ",broker,"\n\n")
        client.connect(broker)
        client.subscribe("CAB0103UK003/tcn")
        client.loop_forever()

    except KeyboardInterrupt:
        print("keyboard interupt detected")
    finally:
        print("Final block executed")
        client.loop_stop()
        client.disconnect()

