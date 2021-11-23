"""
FILE FOR READ WRITE FROM PLC AND IO AND SENDING THE DATA OVER CHANNEL FOR MAINTENANCE VIEW
"""

from optivity import properties
if properties.IO_CONTROLLER_PLUGGED:
    from io_plc_logic.gpio_control_api import gpio_control
if properties.PLC_CONTROLLER_PLUGGED:
    from pyModbusTCP.client import ModbusClient
import time
import json
import websocket
from database import maintenance_db as mdb
from database import util_db as udb
from common_logger.common_util import log
from optivity import properties
import configparser
import atexit


def config_file_parser(file_path=properties.MAINTENANCE_INI_FILE_PATH):
    config = configparser.ConfigParser() # instantiate
    config.read(file_path) # parse existing file
    return config
def set_value_config_file(section, key, value,file_path=properties.MAINTENANCE_INI_FILE_PATH):
    config = config_file_parser()
    config.set(section,key,value)
    cfgfile = open(file_path,'w')
    config.write(cfgfile, space_around_delimiters=False)  # use flag in case case you need to avoid white space.
    cfgfile.close()

def get_key_value_from_config_file(section='DATABASE',key='update_maintenance_control_details_from_db'):
    config = config_file_parser()
    value = config.get(section,key)  # read values from a section
    return value

class IOPLCCommunication:
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance == None:
            cls.instance = super(cls,IOPLCCommunication).__new__(cls, *args, **kwargs)
            return cls.instance
        else:
            return cls .instance


    def __init__(self):
        #log.debug("IOPLCCommunication Init called",{"sub_module_id": "IO_PLC_communicate", "tag": "Init", "unique_value": "unique_value1"})
        self.plc_client = None
        self.io_client = None
        self.plc_read_input_register_interval = properties.READ_INPUT_REGISTER_VALUE_INTERVAL
        self.plc_config = None
        self.maintenance_view_ws = None
        self.plc_client_connection_status = False
        self.io_client_connection_status = False
        self.publish_register_data = False
        atexit.register(self.cleanup)

    def get_control_details(self):
        """RETURNS MAINTENANCE VIEW CONTROL DETAILS"""
        try:
            #log.debug("Executing get_control_details", {"sub_module_id": "IO_PLC_communicate", "tag": "get_control_details","unique_value": "unique_value1"})
            rows = mdb.get_control_details_db()
            return rows
        except Exception as e:
            #log.error(e, {"sub_module_id": "IO_PLC_communicate", "tag": "get_control_details","unique_value": "unique_value1"},exc_info=properties.LOGGER_FULL_STACKTRACE)
    #----------PLC----------#
    def get_plc_config(self):
        """READS PLC IP PORT FROM DATABASE LOOKUP TABLE"""
        try:
            #log.debug("Executing get_plc_config",{"sub_module_id": "IO_PLC_communicate", "tag": "get_plc_config", "unique_value": "unique_value1"})
            data = udb.get_plc_details_db()
            self.plc_config = {
                'server_ip': data["plc_address"],
                'server_port': int(data["plc_port"]),
                'auto_open': True,
                'auto_close': False }
        except Exception as e:
            #log.error(e,{"sub_module_id": "IO_PLC_communicate", "tag": "get_plc_config", "unique_value": "unique_value1"},exc_info=properties.LOGGER_FULL_STACKTRACE)

    def connect_to_plc(self):
        """IF CONNECTED TO CONTROLLER INITIALIZES CLIENT OBJECT IF NOT ALREADY INITIALIZED ELSE IT REMAINS NONE"""
        try:
            #log.debug("Executing connect_to_plc",{"sub_module_id": "IO_PLC_communicate", "tag": "connect_to_plc", "unique_value": "unique_value1"})
            if self.plc_config ==None:
                self.get_plc_config()
            if properties.PLC_CONTROLLER_PLUGGED:
                if self.plc_client == None:
                    #CONNECTS TO PLC IF NOT CONNECTED
                    self.plc_client = ModbusClient()
                    self.plc_client.debug(False)
                    self.plc_client.host(self.plc_config["server_ip"])
                    self.plc_client.port(self.plc_config["server_port"])
                    self.plc_client.auto_close(self.plc_config["auto_close"])
                    self.plc_client.auto_open(self.plc_config["auto_open"])
                    self.plc_client_connection_status = self.plc_client.open()
                    #log.debug("Connected to PLC Successfully",{"sub_module_id": "IO_PLC_communicate", "tag": "connect_to_plc","unique_value": "unique_value1"},exc_info=properties.LOGGER_FULL_STACKTRACE)
                else:
                    #log.debug("Already Connected to PLC (as the olc_client object is not none)",{"sub_module_id": "IO_PLC_communicate", "tag": "connect_to_plc","unique_value": "unique_value1"})
            else:
                #log.error("Controller Connected Flag set to False",{"sub_module_id": "IO_PLC_communicate", "tag": "connect_to_plc","unique_value": "unique_value1"},exc_info=properties.LOGGER_FULL_STACKTRACE)
        except Exception as e:
            #log.error(e,{"sub_module_id": "IO_PLC_communicate","tag": "connect_to_plc","unique_value": "unique_value1"},exc_info=properties.LOGGER_FULL_STACKTRACE)

    def read_plc_registers(self,reg_addr,no_of_reg_to_read):
        """READS MULTIPLE REGISTER AND RETURNS A LIST"""
        try:
            if properties.PLC_CONTROLLER_PLUGGED == False: #will send dummy register values
                register_value_list = list(range(reg_addr, no_of_reg_to_read, 1))
            else:
                if self.plc_client == None:  # will connect  to plc if not connected and then will fetch register values from plc
                    self.connect_to_plc()
                register_value_list = self.plc_client.read_holding_registers(reg_addr, no_of_reg_to_read)
                #log.debug("PLC Register First 10 value: {}".format(register_value_list[:10]),{"sub_module_id": "IO_PLC_communicate", "tag": "read_plc_registers","unique_value": "unique_value1"})
            return register_value_list
        except Exception as e:
            #log.error(e, {"sub_module_id": "IO_PLC_communicate", "tag": "read_plc_registers","unique_value": "unique_value1"},exc_info=properties.LOGGER_FULL_STACKTRACE)

    def write_plc_register(self,reg_addr,reg_value):
        """WRITE'S TO A SINGLE PLC REGISTER AND RETURNS THE RESULT"""
        try:
            #log.debug("Executing write_plc_register",{"sub_module_id": "IO_PLC_communicate", "tag": "write_plc_register","unique_value": "unique_value1"})
            if self.plc_client == None:
                self.connect_to_plc()
            res = self.plc_client.write_single_register(reg_addr=reg_addr, reg_value=reg_value)
            return res
        except Exception as e:
            #log.error(e, {"sub_module_id": "IO_PLC_communicate", "tag": "write_plc_register","unique_value": "unique_value1"},exc_info=properties.LOGGER_FULL_STACKTRACE)
            pass

    #----------IO----------#
    def connect_to_io(self):
        try:
            #log.debug("Executing connect_to_io",{"sub_module_id": "IO_PLC_communicate", "tag": "connect_to_io", "unique_value": "unique_value1"})
            if properties.IO_CONTROLLER_PLUGGED == True:
                self.io_client = gpio_control()
                self.io_client_connection_status = True
            else:
                #log.error("IO Controller Connected Flag set to False",{"sub_module_id": "IO_PLC_communicate", "tag": "connect_to_io","unique_value": "unique_value1"},exc_info=properties.LOGGER_FULL_STACKTRACE)
        except Exception as e:
            #log.error(e,{"sub_module_id": "IO_PLC_communicate", "tag": "connect_to_io", "unique_value": "unique_value1"},exc_info=properties.LOGGER_FULL_STACKTRACE)

    def read_io_registers(self):
        """READS MULTIPLE REGISTER AND RETURNS A LIST"""
        try:
            #log.debug("Executing read_io_registers",{"sub_module_id": "IO_PLC_communicate", "tag": "read_io_registers", "unique_value": "unique_value1"})
            if properties.IO_CONTROLLER_PLUGGED == False: #will send dummy register values
                io_register_values = list(range(-1, -9, -1))
            else:
                if self.io_client == None: #will connect  to plc if not connected and then will fetch register values from plc
                    self.connect_to_io()
                val = self.io_client.write_pin(1, True)
                io_register_values = bin(val)[2:].zfill(8)[::-1]
                #log.debug("returned values {}".format(io_register_values),{"sub_module_id": "IO_PLC_communicate", "tag": "read_io_registers", "unique_value": "unique_value1"})
            return io_register_values
        except Exception as e:
            #log.error(e, {"sub_module_id": "IO_PLC_communicate", "tag": "read_io_registers","unique_value": "unique_value1"},exc_info=properties.LOGGER_FULL_STACKTRACE)

    def write_io_register(self,pin_num,value):
        """WRITE'S TO A SINGLE PLC REGISTER AND RETURNS THE RESULT"""
        try:
            #log.debug("Executing write_io_register",{"sub_module_id": "IO_PLC_communicate", "tag": "write_io_register","unique_value": "unique_value1"})
            if self.io_client == None:
                self.connect_to_io()
            res = self.io_client.write_pin(pin_num,value)
            return res
        except Exception as e:
            #log.error(e, {"sub_module_id": "IO_PLC_communicate", "tag": "write_io_register","unique_value": "unique_value1"}, exc_info=properties.LOGGER_FULL_STACKTRACE)
            pass

    def map_io_plc_register_value_and_publish(self):
        """GETS REGISTER_VALUE_LIST(IO and or PLC), CONTROL_DETAILS FROM DB AND MAPS THEM RESPECTIVELY AND PUBLISH OVER CHANNEL"""
        try:
            #log.debug("Executing map_io_plc_register_value_and_publish", {"sub_module_id": "IO_PLC_communicate", "tag": "map_io_plc_register_value_and_publish","unique_value": "unique_value1"})
            self.maintenance_view_ws = websocket.WebSocket()
            self.maintenance_view_ws.connect('ws://'+str(properties.HOST_IP)+':'+str(properties.PORT)+'/ws/'+str(properties.MAINTENANCE_VIEW_SUB_WEB_SOCKET_URL)+'/')
            #log.debug("Connected to Maintenance socket:" +'ws://'+str(properties.HOST_IP)+':'+str(properties.PORT)+'/ws/'+str(properties.MAINTENANCE_VIEW_SUB_WEB_SOCKET_URL)+'/',{"sub_module_id": "IO_PLC_communicate", "tag": "map_io_plc_register_value_and_publish","unique_value": "unique_value1"})
            #log.debug("Starting loop for fetching register data and publishing on channel",{"sub_module_id": "IO_PLC_communicate", "tag": "map_io_plc_register_value_and_publish","unique_value": "unique_value1"})
            while self.publish_register_data:
                plc_register_value_list = self.read_plc_registers(reg_addr=properties.START_REGISTER_ADDRESS, no_of_reg_to_read=properties.NO_OF_REGISTER_TO_READ)  # getting plc register value
                io_register_value_list = self.read_io_registers() # getting io register value
                fetch_flag = get_key_value_from_config_file(section='DATABASE',key='update_maintenance_control_details_from_db')
                if fetch_flag == 'True':  # as config parser requires values in string format
                    #log.debug("Maintenance Page clicked or refreshed hence fetching control_details values fron DB",{"sub_module_id": "IO_PLC_communicate", "tag": "map_io_plc_register_value_and_publish","unique_value": "unique_value1"})
                    control_details = self.get_control_details()
                    set_value_config_file(section='DATABASE', key='update_maintenance_control_details_from_db',value='False')
                    #log.debug("Control Details Fetched hence changing the (update_maintenance_control_details_from_db) flag to false",{"sub_module_id": "IO_PLC_communicate", "tag": "map_io_plc_register_value_and_publish","unique_value": "unique_value1"})
                control_event_register_value_list = []
                for x in control_details:
                    temp_dict = {}
                    temp_dict["maintenance_id"] = x["maintenance_id"]
                    temp_dict["read_register"] = x["read_register"]
                    if x["controller_type"].lower() == 'plc':
                        temp_dict["value"] = plc_register_value_list[int(x["read_register"])]  # will read the corresponding index from the plc_register_value_list
                    elif x["controller_type"].lower() == 'io':
                        temp_dict["value"] = io_register_value_list[int(x["read_register"])-1]  # will read the corresponding index from the io_pin_values_list
                    control_event_register_value_list.append(temp_dict)
                self.maintenance_view_ws.send(json.dumps(control_event_register_value_list))
                time.sleep(properties.READ_INPUT_REGISTER_VALUE_INTERVAL)
                if properties.PRINT_FETCHED_CONTROL_EVENT_REGISTER_VALUES :
                    #log.info("FETCHED_CONTROL_EVENT_REGISTER_VALUES: {}".format(control_event_register_value_list),{"sub_module_id": "IO_PLC_communicate", "tag": "map_io_plc_register_value_and_publish","unique_value": "unique_value1"})

        except BaseException as e:
            #log.error(e, {"sub_module_id": "IO_PLC_communicate", "tag": "map_publish_register_value","unique_value": "unique_value1"}, exc_info=properties.LOGGER_FULL_STACKTRACE)
            pass

    def cleanup(self):
        try:
            #log.info("IOPLCCommunication Destructor called",{"sub_module_id": "IO_PLC_communicate", "tag": "Cleanup", "unique_value": "unique_value1"})
            if self.plc_client_connection_status:
                self.plc_client.close()
            #if self.io_client != None: #IO (gpio module object) will call the destructor and which will shutdown all lights when shutdown abruptly or normally
            if True:    
                #log.info("********************called",{"sub_module_id": "IO_PLC_communicate", "tag": "Cleanup", "unique_value": "unique_value1"})
                del self.io_client
                #log.debug("IO connection Closed", {"sub_module_id": "IO_PLC_communicate", "tag": "Cleanup","unique_value": "unique_value1"})
            if self.maintenance_view_ws:
                self.maintenance_view_ws.close()
                #log.debug("Closed Maintenance View WebSocket Connection:" + 'ws://' + str(properties.HOST_IP) + ':' + str(properties.PORT) + '/ws/' + str(properties.MAINTENANCE_VIEW_SUB_WEB_SOCKET_URL) + '/',{"sub_module_id": "IO_PLC_communicate", "tag": "Cleanup","unique_value": "unique_value1"})
        except Exception as e:
            #log.error(e,{"sub_module_id": "IO_PLC_communicate", "tag": "Cleanup", "unique_value": "unique_value1"},exc_info=properties.LOGGER_FULL_STACKTRACE)


io_plc_obj = IOPLCCommunication()
print("inside io_plc_communicate io_plc_obj:",io_plc_obj)

def start_read_plc_and_io():
    try:
        #log.debug("Executing start_read_plc_and_io",{"sub_module_id": "IO_PLC_communicate", "tag": "start_read_plc_and_io","unique_value": "unique_value1"})
        io_plc_obj.publish_register_data = True
        io_plc_obj.map_io_plc_register_value_and_publish()
    except Exception as e:
        #log.error(e, {"sub_module_id": "IO_PLC_communicate", "tag": "Cleanup", "unique_value": "unique_value1"},exc_info=properties.LOGGER_FULL_STACKTRACE)


def stop_read_plc_and_io():
    """SETS THE PUBLISH FLAG FALSE WHICH IS CHECKED IN FUNCTION: map_io_plc_register_value_and_publish AFTER RECIEVED FALSE THE FUNCTION TERMINATES """
    try:
        #log.debug("Executing stop_read_plc_and_io", {"sub_module_id": "IO_PLC_communicate", "tag": "write_to_plc_helper","unique_value": "unique_value1"})
        io_plc_obj.publish_register_data = False
    except Exception as e:
        #log.error(e, {"sub_module_id": "IO_PLC_communicate", "tag": "Cleanup", "unique_value": "unique_value1"},exc_info=properties.LOGGER_FULL_STACKTRACE)


def write_to_plc_helper(reg_addr, reg_value):
    """HELPER FUNCTION TO WRITING TO PLC AS WAS GETTING ERROR IF THE OBJECT WAS IMPORTED TO OTHER FILE AND USED DIRECTLY"""
    try:
        #log.debug("Executing write_to_plc_helper",{"sub_module_id": "IO_PLC_communicate", "tag": "write_to_plc_helper","unique_value": "unique_value1"})
        io_plc_obj.write_plc_register(reg_addr=reg_addr, reg_value=reg_value)
    except Exception as e:
        #log.error(e, {"sub_module_id": "IO_PLC_communicate", "tag": "write_to_plc_helper", "unique_value": "unique_value1"},exc_info=properties.LOGGER_FULL_STACKTRACE)


def write_to_io_helper(pin_num, value):
    """HELPER FUNCTION TO WRITING TO IO AS WAS GETTING ERROR IF THE OBJECT WAS IMPORTED TO OTHER FILE AND USED DIRECTLY"""
    try:
        #log.debug("Executing write_to_plc_helper", {"sub_module_id": "IO_PLC_communicate", "tag": "write_to_plc_helper","unique_value": "unique_value1"})
        io_plc_obj.write_io_register(pin_num, value)
    except Exception as e:
        #log.error(e, {"sub_module_id": "IO_PLC_communicate", "tag": "Cleanup", "unique_value": "unique_value1"},exc_info=properties.LOGGER_FULL_STACKTRACE)

#switch off all lights

def falsify_all_registers():
    """WRITS 0 TO ALL PINS"""
    try:
        #log.debug("Executing falsify_all_registers", {"sub_module_id": "IO_PLC_communicate", "tag": "falsify_all_registers","unique_value": "unique_value1"})
        for x in range(1,9):
            io_plc_obj.write_io_register(x, 0)
    except Exception as e:
        #log.error(e, {"sub_module_id": "IO_PLC_communicate", "tag": "falsify_all_registers", "unique_value": "unique_value1"},exc_info=properties.LOGGER_FULL_STACKTRACE)
