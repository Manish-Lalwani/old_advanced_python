import websocket
import json


ws = websocket.WebSocket()
ws.connect('ws://localhost:8000/ws/new_test_case')
data = ws.recv()
ws.send(json.dumps({'value': 1}))