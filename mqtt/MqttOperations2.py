#xml implementation
import paho.mqtt.client as mqtt
from logger import Logger
import logging
import time
#import my_beautify as mb
import inspect
import psycopg2
import json
from datetime import datetime,timedelta

details_flag =0

l1 = Logger(console_output_flag=1,filename='mqtt_client_log',stream_handler_level=logging.INFO,file_handler_level=logging.DEBUG)
log = l1.get_logger()

##print(log.handlers,log.level)

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
        test_case_id = self.temp_database_write(msg)
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
            message = json.loads(message1.payload.decode("utf-8"))
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
                message["testCaseId"],
                message["cabinetId"],
                message["testGroup"][0]["testGroupName"],
                message["testGroup"][0]["testSuite"][0]["testSuiteName"],
                message["testGroup"][0]["testSuite"][0]["testCase"][0]["testCaseName"],
                message["testGroup"][0]["testSuite"][0]["testCase"][0]["meterId"],
                message["testGroup"][0]["testSuite"][0]["testCase"][0]["actions"],
                schedule_time
                )

            cursor.execute(query, record)
            #message_id = cursor.fetchone()[0]
            conn.commit()
            log.info("Database Write Successful for TestCaseID:{} ".format(message["testCaseId"]))

            return message["testCaseId"]
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
        time.sleep(2)  # temp
        log.info("-------------------------------------")
        log.info("FROM HERE ONLY FUNCTIONS CALL ARE EXECUTED FOR DEMO PURPOSE NO OPERATIONS ARE BEING PERFORMED")
        log.info("TestCase:{} is scheduled for now".format(test_case_id))
        self.temp_controller_instructor(test_case_id)


    def  db_status_updater(self,test_case_id,status):
        """THIS FUNCTION WILL BE CALLED TO UPDATE/CHANGE THE STATUS OF TASK IN DATABASE

        """
        time.sleep(2)  # temp
        log.info("Successfully change status to {} for TestCase:{}".format(status,test_case_id))

    def temp_controller_instructor(self,test_case_id):
        """THIS FUNCTION WILL BE CALLED WHEN A TEST CASE IS SCHEDULED FOR RUN
            EVERY CALL WILL BE FOR A DIFFEREN TEST CASE AND WILL BE RUNNING ON SEPARATE THREAD
        1. Will fetch respective TestCase data from database
        2. Give Instruction to controller for starting the task
        3. Get ACKNOWLEDGMENT FROM controller
        3. WAIT FOR STATUS OF RUNNING TEST ONCE GOT RESULT FROM CONTRLLER WILL CALL db_status_updater FOR UPDATING THE DATABASE"""

        time.sleep(2) #temp
        controller_acknowledgement = 1
        log.info("Sending Instruction for running TestCase:{}".format(test_case_id))


        if controller_acknowledgement ==1:
            status = 'RUNNING'
            time.sleep(2)  # temp
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
            time.sleep(2)  # temp
            log.info("TestCase:{} execution completed successfully, Hence changing the status as {} in Database".format(test_case_id,status))
            self.db_status_updater(test_case_id= test_case_id,status =status)

        else:
            status = 'FAIL'
            log.info("TestCase:{} execution FAILED, Hence changing the status as {} in Database".format(
                test_case_id, status))
            self.db_status_updater(test_case_id=test_case_id, status=status)


if __name__ == "__main__":
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

