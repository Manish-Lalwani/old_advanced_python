import configparser
from pyhive import hive




def read_args():
    """RETURN ARGUMENTS SPECIFIED IN A FILE IN DICTIONARY FORMAT"""
    config_param = {}
    config = configparser.ConfigParser()
    config.read("arguments_local.ini")
    print(f"Entered Config Parameters are as follows:")
    for section in config.sections():
        print(f"\nFor Section {section}:")
        config_param[section] = {}
        for option in config.options(section):
            config_param[section][option] = config.get(section, option)
            print(f"{option}:{config_param[section][option]}")
    return config_param

def create_connection(config_param):
    """WILL RETURN CONNECTION OBJECT"""
    con = hive.Connection(host=config_param['Conn_Arguments']["host"],
                          database=config_param['Conn_Arguments']["database"],username=config_param['Conn_Arguments']["username"],
                          )
    return con




def execute_query(con,query):
    """RETURNS RESULT OF THE EXECUTED QUERY IF ANY"""
    res = None
    cur = con.cursor()
    cur.execute(query)
    res = cur.fetchall()
    print(f"result of executed query is: {res}")




if __name__ == "__main__":
    config_param = read_args()
    conn = create_connection(config_param)
    query = """SELECT * FROM table_name""" ###change table name here
    res = execute_query(con,query)
