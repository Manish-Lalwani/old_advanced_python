import pysftp


hostname = "127.0.0.1"
username = "xyz"
password = "Dora456."



with pysftp.Connection(host=hostname, username=username, password=password) as sftp:
	print("Connection successfully established ... ")