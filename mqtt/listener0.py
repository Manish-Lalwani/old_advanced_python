import paho.mqtt.client as mqtt
import time

broker = 'test.mosquitto.org'
client = mqtt.Client("c1")


print("Connecting to broker",broker)
client.connect(broker)
print("connected to broker")
time.sleep(4)
client.disconnect()
