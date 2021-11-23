#subscribe
import paho.mqtt.client as mqtt
from logger import Logger
import time
import json

message_list = []
l1 = Logger(console_output_flag=0)
log = l1.get_logger()

broker = '172.16.1.127'
topic = "CAB0103UK003/tcn"

def on_connect(client, userdata, flags, rc):
    print("=========================ON Connect:========================= ")
    print("Connected successfully to Broker: ",broker) if rc == 0 else print("Bad connection to Broker: {}, RETURNED CODE: {}".format(broker,rc))
    print("Subscribed successfully to topic: ",topic) if client.subscribe(topic) else print("Error in subscription to topic: ",topic)

def on_log(client, userdata, level, buf):
    #print("=========================ON LOG:========================= ")
    #print("CLIENT: {}, USERDATA: {}, LEVEL: {}, BUFFER: {}".format(client,userdata,level,buf))
    pass

def on_disconnect(client, userdata, flags, rc=None):
    print("=========================ON DISCONNECT====================")
    print("RC COde: ",rc)

def on_message(client,userdata,msg):
    print("=========================ON MESSAGE:=========================")
    print("Recieved messge is: ",str(msg.payload.decode("utf-8")))
    message_list
    #print("TYpe is ",type(msg))
    #message = json.loads(str(msg.payload.decode("utf-8")))

    #client.publish("CAB0103UK003/tcn", "Recieved Test case {}".format(message["cabinetId"]))





client = mqtt.Client("c1")

client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_log = on_log
client.on_message = on_message

try:
    print("Connecting to Broker: ",broker)
    client.connect(broker)
    #client.subscribe("iot_data")
    client.loop_forever()

except KeyboardInterrupt:
    print("Keyboard interrupt detected")
    client.loop_stop()
    client.disconnect()

