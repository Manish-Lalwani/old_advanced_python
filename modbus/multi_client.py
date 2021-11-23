#THis is client

from pyModbusTCP.client import ModbusClient
import time
import threading

server_config = {
    'server_ip' :'192.168.3.250',
    'server_port': 502,
    'auto_open': True,
    'auto_close': False
}



# print (client)



# client2.debug(True)
# client2.host(server_config["server_ip"])
#client.port(server_config["server_port"])
#client.auto_close(server_config["auto_open"])
#client.auto_open(server_config["auto_close"])

# print(client.open(),"---client open")
class IOCOMM:
    def __init__(self):
        self.client = ModbusClient()
        self.client.debug(True)
        self.client.host(server_config["server_ip"])
        self.client.port(server_config["server_port"])
        self.client.auto_open(server_config["auto_open"])
        self.client.auto_close(server_config["auto_close"])

        print(self.client.open(),"---client open")
        self.lock = threading.Lock()

    #read register
    def my_read_input_registers(self,reg_addr,no_of_reg_to_read):
        while True:
            print("waiting for lock in read")
            self.lock.acquire()
            register_value = self.client.read_holding_registers(reg_addr,no_of_reg_to_read)
            print("Register_value is\n",register_value)
            self.lock.release()
            time.sleep(0.5)
            print("lock released read")

    #write register
    def my_write_single_register(self,reg_addr,reg_value):
        while True:
            print("waiting for lock in write")
            self.lock.acquire()
            res =self.client.write_single_register(reg_addr=reg_addr,reg_value=reg_value)
            print("written to register @{} value {}".format(reg_addr,reg_value))
            self.lock.release()
            time.sleep(0.5)
            print("lock released write")


        #client.write_multiple_registers()

if __name__ == "__main__":
    obj = IOCOMM()
    x = threading.Thread(target = obj.my_read_input_registers,args=(1,2,))
    y = threading.Thread(target = obj.my_write_single_register,args=(2,3,))

    x.start()
    y.start()

    while True:
        time.sleep(10)

    my_write_single_register(2,24)
    while True:
        my_read_input_registers(2,1)
        time.sleep(3)

    obj = IOCOMM()


    # x = threading.Thread(target = my_read_input_registers,args=(1,2,))
    # y = threading.Thread(target = my_write_single_register,args=(2,3,))