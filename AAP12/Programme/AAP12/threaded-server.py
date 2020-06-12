import socket #Import socket module
import threading


s = socket.socket() #Create a socket Object 
host = '' #unspecified ip - all interfaces on host
port = 12345 #Reserve a port for your service
s.bind((host, port)) #Bind to the port
s.listen(5)


def new_client(client, connection):
    ip = connection[0]
    port = connection[1]
    print(f"the new connection was made form IP : {ip}, and port: {port}!")
    while True:
        msg = client.recv(1024)
        print(f"The client with Port:{port} said: {msg.decode()}")
        reply = f"You told me: {msg.decode()}"
        client.sendall(reply.encode("UTF8"))

while True:  
    client, ip = s.accept()
    threading._start_new_thread(new_client, (client, ip))