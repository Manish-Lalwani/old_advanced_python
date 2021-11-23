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

def listener():
    while True:
        result = json.loads(ws.recv())
        if result["value"] != "Ping: Python Client" and result["value"] != "Ping: controller":
            print("result is:",result)

def ping_send1():
        while True:
            dict1 = {'value': 'Ping: Python Client'}
            #ws.send(json.dumps({'value': 'ping'}))
            ws.send(json.dumps(dict1))
            time.sleep(10)



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

        self.root = None #temp 5oct

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
        time.sleep(1)
        self.temp_message_ack(test_case_id)

        #trmp calling status_checker after wards it will on it own run on a separate thread: 02
        self.test_case_schedule_checker(test_case_id)
        #temp end:02
        log.info("Going for sleep for 10 sec")
        time.sleep(1)
        ###self.temp_res_publish(test_case_id)




    def get_client(self):
        return self.client

    def temp_database_write(self,message1):
        try:
            ##print("in temp database type of message",type(message1))
            root = et.fromstring(message1)
            self.root = root
            self.message1 = message1
            print("Temp: root {} and its Type {} is".format(root,type(root)))
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

    def temp_res_publish(self,test_case_id,status):
        try:
            self.client_publish = mqtt.Client("result_publisher")
            self.client_publish.on_connect = self.on_connect
            self.client_publish.on_disconnect = self.on_disconnect
            self.client_publish.on_log = self.on_log
            # self.client_publish.on_message = self.on_message
            self.client_publish.connect(self.broker)
            self.client_publish.publish('SS/tcnres', "{}:{}".format(test_case_id,status))
            log.info("Result sent successfully for TestCaseID:{}".format(test_case_id))

        except Exception as e:
            log.error(e)





    #Test Case status related function
    def test_case_schedule_checker(self,test_case_id=000): #temp passing test_case_id afterwards will fetch from database
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

    def temp_controller_instructor(self,test_case_id):
        """THIS FUNCTION WILL BE CALLED WHEN A TEST CASE IS SCHEDULED FOR RUN
            EVERY CALL WILL BE FOR A DIFFEREN TEST CASE AND WILL BE RUNNING ON SEPARATE THREAD
        1. Will fetch respective TestCase data from database
        2. Give Instruction to controller for starting the task
        3. Get ACKNOWLEDGMENT FROM controller
        3. WAIT FOR STATUS OF RUNNING TEST ONCE GOT RESULT FROM CONTRLLER WILL CALL db_status_updater FOR UPDATING THE DATABASE"""

        log.info("Writing current TestCase to Secondary Table")
        self.db_status_updater(test_case_id=test_case_id,status='Sending',mode = 'Insert')
        log.info("TestCase Inserted Successfully")

        log.info("Sending Instruction for running TestCase:{} using WebSocket".format(test_case_id))
        ws.send(json.dumps({'value': 'Message:Python Client:{}'.format(self.message1)}))


    def controller_status_recieve_execute(self,test_case_id,status):

        print("Temp status is {}".format(status))
        if status =='RUNNING':
            log.info("Acknowledged by controller successfully, Hence changing the status as RUNNING in Database")
            self.db_status_updater(test_case_id= test_case_id,status =status,mode='update')


        elif status == 'PASS':
            log.info("Changing the Database status as PASS")
            self.db_status_updater(test_case_id=test_case_id, status=status,mode='update')
            self.temp_res_publish(test_case_id=test_case_id,status='PASS')


        elif status == 'FAIL':
            log.info("TestCase:{} execution completed successfully, Hence changing the status as {} in Database".format(test_case_id,status))
            self.db_status_updater(test_case_id= test_case_id,status =status,mode='update')
            self.temp_res_publish(test_case_id=test_case_id, status='FAIL')

        else:
            status = 'ERROR'
            log.info("TestCase:{} execution FAILED, Hence changing the status as {} in Database".format(
                test_case_id, status))
            self.db_status_updater(test_case_id=test_case_id, status='ERROR',mode='update')
            self.temp_res_publish(test_case_id=test_case_id, status='PASS')


    def  db_status_updater(self,test_case_id,status,mode):
        """THIS FUNCTION WILL BE CALLED TO First Insert then UPDATE/CHANGE THE STATUS OF TASK IN DATABASE

        """

        conn_dict = {
            'host': "localhost",
            'database': "TempTestCaseDB2",
            'user': "postgres",
            'password': "griffyn"}

        conn = psycopg2.connect(host=conn_dict['host'], database=conn_dict['database'], user=conn_dict['user'],
                                password=conn_dict['password'])
        log.info("Connection successful to Database: {} ".format(conn_dict['database']))
        cursor = conn.cursor()
        if mode == 'Insert':
            root = self.root
            start_time = datetime.now()
            end_time = datetime.now()
            status = 'Sending'
            status_integer = -1
            # insert query
            query = """INSERT INTO test_data_table2(test_case_id,test_case,on_meter,start_time,end_time,status,status_priority) VALUES (%s,%s,%s,%s,%s,%s,%s)"""
            record = (
                root[2].text,  # test_case_ud
                #root[0].text,  # cabinet_id
                #root[1][1].text,  # test_group_name
                #root[1][0][0].text,  # test_suite_name
                root[1][0][1][1].text,  # test_case_name
                root[1][0][1][0].text,  # meter_id
                #root[1][0][1][2].text,  # action
                start_time,
                end_time,
                status,
                status_integer
            )

            cursor.execute(query, record)
            # message_id = cursor.fetchone()[0]
            conn.commit()
            log.info("Database Insert Successful for TestCaseID:{} ".format(root[2].text))

        else: # mode is update
            query = """UPDATE test_data_table2 SET status = '{}' WHERE test_case_id = {} ;""".format(status,test_case_id)
            cursor.execute(query)
            # message_id = cursor.fetchone()[0]
            conn.commit()

        log.info("Successfully change status to {} for TestCase:{}".format(status,test_case_id))


    #websocket ping,listen
    def listener(self):
        while True:
            result = json.loads(ws.recv())
            #if result["value"] != "Ping: Python Client" and result["value"] != "Ping: controller":
            if ("Ping" not in result["value"]) and ("Client" not in result["value"]) :
                print("result is:", result) ##'value': 'Message: controller:Test_Case_ID: Running'
                list1 = str(result["value"]).split(":")
                print("Temp :list is:{}".format(list1))
                self.controller_status_recieve_execute(test_case_id=list1[2], status=list1[3])


    def ping_send1(self):
        while True:
            dict1 = {'value': 'Ping: Python Client'}
            # ws.send(json.dumps({'value': 'ping'}))
            ws.send(json.dumps(dict1))
            time.sleep(10)


if __name__ == "__main__":
    print("Test In main")
    #broker = '172.16.1.127'
    broker = '127.0.0.1'
    obj1 = MqttClient(broker = broker,topic = 'CAB0103UK003/tcn',client_name='test_case_subscriber')
    client = obj1.get_client()

    listener_start = threading.Thread(target=obj1.listener)
    listener_start.start()

    ping_start = threading.Thread(target=obj1.ping_send1)
    ping_start.start()


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

