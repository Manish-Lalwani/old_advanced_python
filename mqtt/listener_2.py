import paho.mqtt.client as mqtt
import time


def on_connect(client, userdata, flags, rc):
    print("==========Inside func_on_connect==========")
    print("CLIENT: {}".format(client))
    print("USERDATA: {}".format(userdata))
    print("FLAGS: {}".format(flags))
    print("rc: {}".format(rc))

    if rc == 0:
        print("Connected successfully")
    else:
        print("Bad connection RETURNED CODE: {}".format(rc))
    print("==========End func_on_connect==========\n\n\n")


def on_log(client, userdata, level, buf):
    print("==========Inside func_on_log==========")
    print("CLIENT: {}".format(client))
    print("USERDATA: {}".format(userdata))
    print("LEVEL: {}".format(level))
    print("buf: {}".format(buf))
    print("==========End func_on_log==========\n\n\n")


broker = 'test.mosquitto.org'
client = mqtt.Client("c1")

client.on_connect = on_connect
client.on_log = on_log

print("Connecting to broker: ",broker)
client.connect(broker)
client.loop_start()
time.sleep(4)
client.loop_stop()

client.disconnect()

