import websocket
import json
import time

ws = websocket.WebSocket()
ws.connect('ws://localhost:8000/ws/new_test_case')

# def listener():
#     while True:
#         result = json.loads(ws.recv())
#         if result["value"] != "Ping: Python Client" and result["value"] != "Ping: controller":
#             print("result is:",result)



class WSListener():
    def __init__(self,url):
        self.ws = websocket.WebSocket()
        self.ws.connect(url)

    def ping_send(self, message='Ping: listener Python Client'):
        """This function is used to keep the websocket connection active by sending ping every 10 sec"""
        while True:
            dict1 = {'value': message}
            self.ws.send(json.dumps(dict1))
            time.sleep(10)

    def listener(self):
        """This method needs to be overrided for retrieving particular messages"""
