#THis is client

from pyModbusTCP.client import ModbusClient
import time

server_config = {
    'server_ip' :'192.168.3.250',
    'server_port': 502,
    'auto_open': True,
    'auto_close': False
}

client = ModbusClient()
print (client)
client.debug(True)

client.host(server_config["server_ip"])
#client.port(server_config["server_port"])
#client.auto_close(server_config["auto_open"])
#client.auto_open(server_config["auto_close"])

print(client.open(),"---client open")

#read register
def my_read_input_registers(reg_addr,no_of_reg_to_read):
    while True:
        register_value = client.read_holding_registers(reg_addr,no_of_reg_to_read)
        print("Register_value is\n",register_value)
        time.sleep(2)

#write register
def my_write_single_register(reg_addr,reg_value):
    res =client.write_single_register(reg_addr=reg_addr,reg_value=reg_value)
    print("written to register @{} value {}".format(reg_addr,reg_value))


    #client.write_multiple_registers()

if __name__ == "__main__":
    my_write_single_register(2,24)
    while True:
        my_read_input_registers(2,1)
        time.sleep(3)

