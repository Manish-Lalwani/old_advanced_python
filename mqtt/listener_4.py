#subscribe
import paho.mqtt.client as mqtt
import my_beautify as mb
import inspect
import time

#stack = inspect.stack()
#mb.details(stack, details_flag)
def on_connect(client, userdata, flags, rc):
    print("==========Inside func_on_connect==========")
    client.subscribe("iot_data")
    # print("CLIENT: {}".format(client))
    # print("USERDATA: {}".format(userdata))
    # print("FLAGS: {}".format(flags))
    # print("rc: {}".format(rc))

    if rc == 0:
        print("Connected successfully")
    else:
        print("Bad connection RETURNED CODE: {}".format(rc))


def on_log(client, userdata, level, buf):
    print("==========Inside func_on_log==========")
    # print("CLIENT: {}".format(client))
    # print("USERDATA: {}".format(userdata))
    # print("LEVEL: {}".format(level))
    print("buf: {}".format(buf))


def on_disconnect(client, userdata, flags, rc=None):
    print("==========Inside func_on_connect==========")
    # print("CLIENT: {}".format(client))
    # print("USERDATA: {}".format(userdata))
    # print("FLAGS: {}".format(flags))
    print("rc: {}".format(rc))

def on_message(client,userdata,msg):
    print("==========Inside func_on_message==========")
    print("MESSAGE IS:",msg)

broker = '172.16.1.127'
client = mqtt.Client("c1")

client.on_connect = on_connect
#client.on_disconnect = on_disconnect
#client.on_log = on_log
client.on_message = on_message

try:
    print("Connecting to broker: ",broker)
    client.connect(broker)
    #client.subscribe("iot_data")
    client.loop_forever()




except KeyboardInterrupt:
    client.loop_stop()
    client.disconnect()

