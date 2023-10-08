import socket

host = "YOUR IP"
port = 9998

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.connect((host,port))

while True:
    print("Get Hacked Lol")