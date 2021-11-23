from channels.generic.websocket import AsyncWebsocketConsumer
import json
#import my_beautify as mb
import inspect
import os



def details(stack, on_flag=1):
    if on_flag == 1:
        stack = stack
        current_func = stack[0].function  # stack[0][0].f_code.co_name
        if "self" in stack[0][0].f_locals:  # checking if function in class or direct
            current_class = stack[0][0].f_locals["self"].__class__.__name__
        else:
            current_class = "None"

        current_func_lineno = stack[0].lineno

        head, tail = os.path.split(stack[0].filename)  # as was getting ful path spliting the file name
        current_filename = tail

        caller_func = stack[1][0].f_code.co_name

        if "self" in stack[1][0].f_locals:
            caller_class = stack[1][0].f_locals["self"].__class__.__name__
        else:
            caller_class = "None"
        caller_func_lineno = stack[1].lineno
        head, tail = os.path.split(stack[1].filename)
        caller_filename = tail
        # print("_____________________________________________________________________________________________")
        # print("---------------------------------------------------------------------------------------------")
        # print("=============================================================================================")
        # print("Executing {}() {} - {} {}-->Caller {}() {} - {} {} ".format(current_func,current_func_lineno,current_class,current_filename, caller_func,caller_func_lineno,caller_class,caller_filename))
        str1 = "Executing [{}() {} - {} {}]".format(current_func, current_func_lineno, current_class, current_filename)
        str2 = "Caller [{}() {} - {} {}] ".format(caller_func, caller_func_lineno, caller_class, caller_filename)

        # print('%-65s | %-65s' % (str1, str2)) # '-' for left align, 65 total space given, 's for string'

        str3 = '%-65s | %-65s' % (str1, str2)
    # log1.error("_____________________________________________________________________________________________")
    # log1.error(str3)

    ######print("{}-->{}".format(str2,str1))
    # len(str1)
    # print("{} {}".format(str1,str2.rjust(100-len(str1),'-')))
    # print("length is :",len(str1))
    ###print('%-50s%-12s' % (str1, str2)
    # print("L {:^20} R".format(str1))
    # # Example 1
    # print('L {:<20} R'.format('x'))
    # # Example 2
    # print('L {:^20} R'.format('x'))
    # # Example 3
    # print('L {:>20} R'.format('x'))

    # print(str1.rjust(40,'+'))


class DashConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.group_name = 'dashboard'
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        stack = inspect.stack()
        details(stack, 1)
        print("Got disconnected")

    async def receive(self, text_data=None, bytes_data=None):
        print('recieved message-->', text_data)
        datapoint = json.loads(text_data)
        val = datapoint['value']

        await  self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'function_deprocessing',
                'value': val
            }
        )

    async def function_deprocessing(self, event):
        valother = event['value']
        await self.send(text_data=json.dumps({'value': valother}))
