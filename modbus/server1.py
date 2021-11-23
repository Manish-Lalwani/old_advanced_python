#THis is server it will reside on PLC
#will be getting this file
from pyModbusTCP.server import ModbusServer

config ={
    "host": "localhost",
    "port": 6999,
}



if __name__ == "__main__":
    server = ModbusServer(host=config["host"],port=config["port"] )
    server.start()

