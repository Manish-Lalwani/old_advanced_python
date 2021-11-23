import socket

#https://www.geeksforgeeks.org/socket-programming-python/
s = socket.socket()
print("socket created successfully")

ip = '' # ip is kept blank so that it can listen to connection from other networks
port = 12345
s.bind((ip,port))
s.listen(5)
print("Socket is active and listening on port 12345")


while True:
    c,addr = s.accept()
    print("C:{}\naddr:{}".format(c,addr))



