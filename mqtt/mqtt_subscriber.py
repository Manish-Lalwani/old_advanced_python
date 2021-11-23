from MqttOperations import MqttClient

def over_ridded_message(client, userdata, msg):
    print("over ridded message successfully called")


if __name__ == "__main__":
    try:
        broker = '172.16.1.127'
        obj1 = MqttClient(broker = broker,topic = 'iot_data',client_name='a2')
        obj1.on_message = over_ridded_message
        client = obj1.get_client()

        print("Connecting to Broker: ",broker)
        client.connect(broker)
        client.subscribe("iot_data")
        client.loop_forever()

    except KeyboardInterrupt:
        print("keyboard interupt detected")
    finally:
        print("Final block executed")
        client.loop_stop()
        client.disconnect()

