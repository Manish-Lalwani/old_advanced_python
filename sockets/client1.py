import socket
#Server forms the listener socket while client reaches out to the server.

#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s= socket.socket()
#socket.AF_INET is IPV4 address
#socket.SOCK_STREAM means connection oriented TCP protocol

port = 12345
ip = '127.0.0.1'
s.connect((ip,port))
print("Socket got cennected successfully")
print(s.recv(1024))
s.close()