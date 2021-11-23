try:
    import os
    import logging
    import logger_base
    import properties
    from datetime import datetime
except ImportError:
    print("All modules are not installed , Kindly run following command in current directory:   pip install requirement.txt ")

class CustomizeLogFormatter(logging.Formatter):
    def format(self, record):
        try:
            record.method = '-'
            record.host = properties.HOST_IP

            if (record.args):
                #record.host = record.args.get('host',properties.HOST_IP)
                #record.tag = record.args.get("tag", "tag")
                pass
            return super().format(record)
        except Exception as e:
            print(e)

l1 = logger_base.LoggerBase(format=CustomizeLogFormatter("""%(asctime)s |%(host)s | %(method)s | %(levelname)s | %(message)s""",
                                                datefmt="%d/%b/%y %H:%M:%S %Z"), logger_user='optivity_logger')
log = l1.get_logger()

try:
    import discord
    from discord import Webhook, RequestsWebhookAdapter, File
except ImportError:
    print("All modules are not installed , Kindly run following command in current directory:   pip install requirement.txt ")

class Logger1:
    def __init__(self):
        self.webhook_id = 701461143214096504
        self.webhook_token = 'ZclvwnGvQEbn2Y2XugIlhIcdJEVFJX5tRkJUe6GS-jdfE9NtYX-lBY38ceSMKn01xB-z'
        self.webhook_obj = None
        self.embed = None
        self.product_list = None

    def authenticate(self):
        self.webhook_obj = Webhook.partial(id=self.webhook_id, token=self.webhook_token,
                                           adapter=RequestsWebhookAdapter())

    def set_embed_new(self, main_data_list, x):  # x is new product index
        # mb.fname_print("set_embed_new")
        self.embed = discord.Embed(title="Found New Row",
                                   description="x{}y{}".format(main_data_list[x][1],
                                                                              main_data_list[x][3]), color=0x00ff00)

        self.embed.set_thumbnail(url=main_data_list[x][4])

        for x, y in zip(main_data_list[x][7], main_data_list[x][8]):
            self.embed.add_field(name=x, value='[ATC]({})'.format(y), inline=True)

    def set_embed_new_3(self,file):
        with open(file) as f:
            data = f.readlines()
        self.embed = discord.Embed(title="Logs",description='test')
        print(data[0])

        for i,x in enumerate(data):
            print(x,"\n\n\n")
            if len(x) > 1022:
                x='-1'
            self.embed.add_field(name=str(i),value=str(x))
    def send(self,file,file_name):
        try:
            self.webhook_obj.send(embed=self.embed,file=File(file,filename=file_name))
        except Exception as e:
            log.error("##Error Occoured")


    def info(self,message):
        log.info(message)
        self.send(f"./logs/log_{datetime.today().strftime('%Y-%m-%d')}.log",file_name=f"{os.path.split(os.path.expanduser('~'))[-1]}_log_{datetime.today().strftime('%Y-%m-%d')}.log")
log1 = Logger1()
