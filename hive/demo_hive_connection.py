import configparser
from pyhive import hive


config_param = None

def read_args():
    """READS ARGUMENT AND ASSIGN IT TO GLOBAL config_param DICT"""
    global config_param
    config_param = {}
    config = configparser.ConfigParser()
    config.read("arguments.ini")
    print(f"Entered Config Parameters are as follows:")
    for section in config.sections():
        print(f"\nFor Section {section}:")
        config_param[section] = {}
        for option in config.options(section):
            config_param[section][option] = config.get(section, option)
            if type(config_param[section][option] )== str : config_param[section][option] = config_param[section][option].strip("'")
            print(f"{option}:{config_param[section][option]}")
    #return config_param


def create_connection():
    """WILL RETURN CONNECTION OBJECT"""
    try:
        print("Connecting to Hive Database")
        print(type(config_param['Conn_Arguments']["kerberos_service_name"]),config_param['Conn_Arguments']["kerberos_service_name"])
        if config_param['Conn_Arguments']["kerberos_service_name"] == 'None':
            con = hive.Connection(host=config_param['Conn_Arguments']["host"],port=int(config_param['Conn_Arguments']["port"]),
                                  database=config_param['Conn_Arguments']["database"],username=config_param['Conn_Arguments']["username"])
        else:
            con = hive.Connection(host=config_param['Conn_Arguments']["host"],port=int(config_param['Conn_Arguments']["port"]),
                              database=config_param['Conn_Arguments']["database"],username=config_param['Conn_Arguments']["username"],
                              auth=config_param['Conn_Arguments']["auth"],kerberos_service_name=config_param['Conn_Arguments']["kerberos_service_name"])
        print("Conencted Successfully")
        return con
    except Exception as e:
        print(e)



def execute_query(query):
    """RETURNS RESULT OF THE EXECUTED QUERY IF ANY"""
    try:
        print("Execution of query started----")
        con = create_connection()
        res = None
        cur = con.cursor()
        cur.execute(query)
        res = cur.fetchall()
        print("\nResult is :",res)
        return res
    except Exception as e:
        print(e)
    finally:
        if con:
            print("Closing connection")
            con.close()



def get_databases():
    execute_query(con,query="show databases")







if __name__ == '__main__':
    read_args()
    #print("Hive Communication channel established......\n")
    print("Enter query to be executed \n For closing the communication kindly enter exit")
    query = None
    while query != 'exit':
        query = input("query>")
        execute_query(query)
        print("\n\n")

