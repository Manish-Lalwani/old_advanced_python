#publishing message
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


def on_disconnect(client, userdata, flags, rc=None):
    print("==========Inside func_on_connect==========")
    print("CLIENT: {}".format(client))
    print("USERDATA: {}".format(userdata))
    print("FLAGS: {}".format(flags))
    print("rc: {}".format(rc))
    print("==========End func on_disconnect==========\n\n\n")

try:
    broker = '172.16.1.127'
    client = mqtt.Client("publisher")

    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_log = on_log

    print("Connecting to broker: ",broker)
    client.connect(broker)
    client.loop_start()

    while 1:
        client.publish("CAB0103UK003/tcn","Hello World...")
        time.sleep(1)
finally:
    client.loop_stop()
    client.disconnect()

