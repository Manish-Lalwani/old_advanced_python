from plc_code import IoPlcCommunicate

obj = IoPlcCommunicate()
print("inside plc_code",obj)
#read register
def my_read_input_registers(reg_addr,no_of_reg_to_read):
    #while True:
        register_value = obj.client.read_holding_registers(reg_addr,no_of_reg_to_read)
        print("Register_value is\n",register_value)
        #time.sleep(2)

#write register
def my_write_single_register(reg_addr,reg_value):
    res =obj.client.write_single_register(reg_addr=reg_addr,reg_value=reg_value)
    print("written to register @{} value {}".format(reg_addr,reg_value))


my_read_input_registers(0,15)
my_write_single_register(2,18)
#my_read_input_registers(0,15)