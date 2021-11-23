#THis is client

from pyModbusTCP.client import ModbusClient
import time


class IoPlcCommunicate:
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance == None:
            new_instance = super(cls,IoPlcCommunicate).__new__(cls,*args, **kwargs)
            cls.instance = new_instance
            return cls.instance
        else:
            print("__new__ executed")
            return cls.instance

    def __init__(self):
        self.server_config = {
            'server_ip' :'192.168.0.5',
            'server_port': 502,
            'auto_open': True,
            'auto_close': False
        }

        self.client = ModbusClient()
        print("client is:",self.client)
        print(self.client)
        self.client.debug(False)

        self.client.host(self.server_config["server_ip"])
        #client.port(server_config["server_port"])
        #client.auto_close(server_config["auto_open"])
        #client.auto_open(server_config["auto_close"])

        print(self.client.open(),"---client open")



obj = IoPlcCommunicate()
print("inside plc_code",obj)
#read register
def my_read_input_registers(reg_addr,no_of_reg_to_read):
        #while True:
            register_value = obj.client.read_holding_registers(reg_addr,no_of_reg_to_read)
            print("Register_value is\n",register_value)
            time.sleep(2)

    #write register
def my_write_single_register(reg_addr,reg_value):
        res =obj.client.write_single_register(reg_addr=reg_addr,reg_value=reg_value)
        print("written to register @{} value {}".format(reg_addr,reg_value))


my_read_input_registers(0,15)
my_write_single_register(1,6)
