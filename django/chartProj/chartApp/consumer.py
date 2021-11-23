from channels.generic.websocket import AsyncWebsocketConsumer
import json

class DashConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.group_name = 'dashboard'
        await self.channel_layer.group_add(self.group_name,self.channel_name)
        await self.accept()

    async def disconnect(self,close_code):
        await self.disconnect()

    async def receive(self, text_data=None, bytes_data=None):
        print('recieved message-->',text_data)
        datapoint = json.loads(text_data)
        val = datapoint['value']

        await  self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'function_deprocessing',
                'value': val
            }
        )


    async def function_deprocessing(self,event):
        valother = event['value']
        await self.send(text_data=json.dumps({'value': valother}))