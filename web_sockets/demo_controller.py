# import websocket
# import json
#
#
# ws = websocket.WebSocket()
# ws.connect('ws://localhost:8000/ws/new_test_case')
#
# ws.send(json.dumps({'value': """<TEST><BUTTON meter_name="meter_0" button="button_1"  wait="5" action="True"/><DISPLAY meter_name="meter_0" display="screen_0" wait="5" text="12345 KWH" /><BUTTON meter_name="meter_0" button="button_0"  wait="5" action="True"/><DISPLAY meter_name="meter_0" display="screen_0" wait="5" text="12345 KWH" /><BUTTON meter_name="meter_0" button="button_1"  wait="5" action="True"/><BUTTON meter_name="meter_0" button="button_0"  wait="3" action="True"/><BUTTON meter_name="meter_0" button="button_0"  wait="2" action="True"/><BUTTON meter_name="meter_0" button="button_0"  wait="2" action="True"/><DISPLAY meter_name="meter_0" display="screen_0" wait="5" text="12345 KWH" /><BUTTON meter_name="meter_0" button="button_1"  wait="5" action="True"/><DISPLAY meter_name="meter_0" display="screen_0" wait="5" text="12345 KWH" /></TEST>"""}))
# #ws.send(json.dumps({'val': '1'}))


#!/usr/bin/env python

# WS client example

import asyncio
import websocket
import threading
import json
import time
import xml.etree.ElementTree as et

# async def hello():
#     uri = "ws://localhost:8000/ws/new_test_case"
#     async with websockets.connect(uri) as websocket:
#         name = input("What's your name? ")

#         await websocket.send(name)
#         print(f"> {name}")

#         greeting = await websocket.recv()
#         print(f"< {greeting}")

# asyncio.get_event_loop().run_until_complete(hello())




ws = websocket.WebSocket()
ws.connect('ws://localhost:8000/ws/loader')


def listener():
    while True:

        message = json.loads(ws.recv())
        print("message[valuw]",message["value"],type(message["value"]))
        if (message["value"] != "Ping: Python Client") and (message["value"] != "Ping: controller") and ("Client" in message["value"]):
            print("message is:",message)
            #msg = str(message["value"].payload.decode("utf-8"))
            list1 = message["value"].split(":")
            message1 = list1[2]
            root = et.fromstring(message1)
            print("root is {}, type is {}".format(root,type(root)))

            time.sleep(4)
            dict2 = {'value': 'Message:controller:{}:RUNNING'.format(root[2].text)}
            ws.send(json.dumps(dict2))
            time.sleep(20)
            dict2 = {'value': 'Message:controller:{}:PASS'.format(root[2].text)}
            ws.send(json.dumps(dict2))



def ping_send1():
        while True:
            dict1 = {
                'value': 'Ping: controller'
            }
            #ws.send(json.dumps({'value': 'ping'}))
            ws.send(json.dumps(dict1))
            time.sleep(10)


if __name__ == "__main__":
    listener_start = threading.Thread(target=listener)
    listener_start.start()

    ping_start = threading.Thread(target=ping_send1)
    ping_start.start()

    #
    # dict2 = {
    #     'value': 'Message: controller:Test_Case_ID: Running'
    # }
    #ws.send(json.dumps(dict2))


    dict2 = {
             'value': 'Status:Cabinet:20'
         }
    ws.send(json.dumps(dict2))
    time.sleep(3)
    dict2 = {
            'value': 'Status:Device:40'
        }
    ws.send(json.dumps(dict2))

    time.sleep(3)
    dict2 = {
        'value': 'Status:Camera:60'
    }
    ws.send(json.dumps(dict2))

    time.sleep(3)
    dict2 = {
        'value': 'Status:Arm:80'
    }
    ws.send(json.dumps(dict2))
    time.sleep(3)
    dict2 = {
            'value': 'Status:Camera 2:100'
        }
    ws.send(json.dumps(dict2))




