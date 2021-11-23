"""
Connecting to HIve Database using pyhive
"""

from pyhive import hive


conn_param = {
	"host_name": "127.0.0.1",
	"port": 10000,
	"username": "hiveuser",
	"password": "hivepassword",
	"database": "default"
}




conn = hive.Connection(host=conn_param["host_name"],username=conn_param["username"])
cur = conn.cursor()
cur.execute("SELECT * from temp1;")
res = cur.fetchall()

print(f"result is: {res}")