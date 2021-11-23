import pyhs2
import logging
if __name__ == "__main__":

    try:
      hive_con =  pyhs2.connect(host='localhost', # Hive server2 IP or host
      port=10000,
      authMechanism="NOSASL",
      user='', # Username
      password='', #User password,
      database='default')
      hive_cur = hive_con.cursor()
      table_body  = '(`Id` BIGINT, `some_field_1` STRING, `some_field_2` STRING ) '
      db_name = "my_db"
      table_name = "my_first_parquete_table"
      table_format = ("PARQUET", "TEXTFILE", "AVRO",)

      # Creating internal Parquet table
      create_tb = ('CREATE TABLE IF NOT EXISTS `%s`.`%s` %s STORED AS %s') % (db_name, tb_name, table_body, table_format[0])
      hive_cur.execute(create_tb)

      # Creating internal Textfile table
      create_tb = ('CREATE TABLE IF NOT EXISTS `%s`.`%s` %s STORED AS %s') % (db_name, tb_name, table_body, table_format[1])
      hive_cur.execute(create_tb)
      hive_cur.close()
      hive_con.close()
    except Exception as e:
        logging.error(str(e))