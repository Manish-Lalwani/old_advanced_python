"""
import pyhs2

with pyhs2.connect(host='beelinehost@hadoop.com',
                    port=10000,
                    authMechanism="KERBEROS")as conn:
"""





import configparser




def read_args():
    """RETURN ARGUMENTS SPECIFIED IN A FILE IN DICTIONARY FORMAT"""
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
    return config_param


# def pyhive_create_connection(config_param):
#     """WILL RETURN CONNECTION OBJECT"""
#     from pyhive import hive
#     con = hive.Connection(host=config_param['Conn_Arguments']["host"],port=int(config_param['Conn_Arguments']["port"]),
#                           database=config_param['Conn_Arguments']["database"],username=config_param['Conn_Arguments']["username"],
#                           auth=config_param['Conn_Arguments']["auth"],kerberos_service_name=config_param['Conn_Arguments']["kerberos_service_name"])
#     return con 


def pyhive_create_connection(config_param):
    """WILL RETURN CONNECTION OBJECT"""
    from pyhive import hive
    con = hive.Connection(host=config_param['Conn_Arguments']["host"],port=int(config_param['Conn_Arguments']["port"]),
                          database=config_param['Conn_Arguments']["database"],username=config_param['Conn_Arguments']["username"],
                          auth=config_param['Conn_Arguments']["auth"],kerberos_service_name=config_param['Conn_Arguments']["kerberos_service_name"])
    print("Conencted to hive database successfully")
    return con 


def pyhs2_create_connection(config_param):
    """WILL RETURN CONNECTION OBJECT"""
    import pyhs2
    con = pyhs2.connect(host=config_param['Conn_Arguments']["host"],port=int(config_param['Conn_Arguments']["port"]),
                          username=config_param['Conn_Arguments']["username"],
                          auth=config_param['Conn_Arguments']["auth"])
    return con


def pyhs2_auth_gssapi_create_connection(config_param):
    """WILL RETURN CONNECTION OBJECT"""
    import pyhs2
    con = pyhs2.connect(host=config_param['Conn_Arguments']["host"],port=int(config_param['Conn_Arguments']["port"]),
                          username=config_param['Conn_Arguments']["username"],
                          auth="GSSAPI")
    return con



def impala_create_connection(config_param):
    #conn = connect(host='hostname.io', port=21050, use_ssl=True, database='default', user='urusername', kerberos_service_name='impala', auth_mechanism = 'GSSAPI')
    #HiveClient(db_host='namenode02.xxx.com', port=10000, authMechanism='GSSAPI', user='hive', password='',
                            # database='data_mp_raw', kbservice='hive')
    from impala.dbapi import connect
    con = connect(host=config_param['Conn_Arguments']["host"],port=int(config_param['Conn_Arguments']["port"]),
                          database=config_param['Conn_Arguments']["database"],user=config_param['Conn_Arguments']["username"],
                          auth_mechanism='GSSAPI',kerberos_service_name='hive')
    return con
def get_databases(con):
    res = None
    cur = con.cursor()
    res = cur.getDatabases()




def execute_query(con,query):
    """RETURNS RESULT OF THE EXECUTED QUERY IF ANY"""
    res = None
    cur = con.cursor()
    cur.execute(query)
    res = cur.fetchall()
    print(f"result of executed query is: {res}")


def beeline_commandline():
    #python 3
    import subprocess
    #cmd = 'beeline -u "jdbc:hive2://node07.foo.bar:10000/...<your connect string>" -e "SELECT * FROM db_name.table_name LIMIT 1;"'
    cmd = 'beeline -u "jdbc:hive2://localhost:10000/;serviceDiscoveryMode=zooKeeper;zooKeeperNamespace=hiveserver2" -e "SELECT * FROM category;" '
    status, output = subprocess.getstatusoutput(cmd)

    if status == 0:
       print(output)    
    else:
       print(status)


if __name__ == "__main__":
    print("=============================================")
    choice = int(input("Select an Option for connecting to hive: \n0. PyHive\n1. Pyhs2 with kerberos\n2. Pyhs2_auth_gssapi_create_connection\n3. Impala\n4. Beeline commandline\n\n Input: "))
    print("=============================================")
    config_param = read_args()
    print("=============================================")




    if choice == 0:
        con = pyhive_create_connection(config_param)
        query = """SELECT * FROM category""" ###change table name here
        res = execute_query(con,query)
        #get_databases(con)


    if choice ==1:
        con = pyhs2_create_connection()
        get_databases(con)

    if choice ==2:
        con =pyhs2_auth_gssapi_create_connection(config_param)
        get_databases(con)

    if choice ==3:
        con = impala_create_connection(config_param)
        query = """SELECT * FROM table_name"""
        execute_query(con,query)

    if choice ==4:
        beeline_commandline()






