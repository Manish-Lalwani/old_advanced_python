#!/usr/bin/env python

# WS client example

import asyncio
import websocket
import threading
import json
import time

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
ws.connect('ws://localhost:8000/ws/new_test_case')

def listener():
    while True:
        result = json.loads(ws.recv())
        if result["value"] != "Ping: Python Client" and result["value"] != "Ping: controller":
            print("result is:",result)
            list1 = str(result["value"]).split(":")


def ping_send1():
        while True:
            dict1 = {'value': 'Ping: Python Client'}
            #ws.send(json.dumps({'value': 'ping'}))
            ws.send(json.dumps(dict1))
            time.sleep(10)


if __name__ == "__main__":
    listener_start = threading.Thread(target=listener)
    listener_start.start()

    ping_start = threading.Thread(target=ping_send1)
    ping_start.start()

    dict2 ={ 'value': 'Message: Python Controller:XML' }
    ws.send(json.dumps(dict2))





