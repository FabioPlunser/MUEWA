import socket
import sys

host = "127.0.0.1"
port = 12345        

# s = socket.socket() 'Create a socket object
# s.connect((host, port)) #Connect to remote TCP service


# or more mordern varaint tries IPV4 and IPV6, multiple addresses

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    while True:
        eingabe = input(f"Eingabe des Cleint: {s.getsockname()[1]}: ")
        if (eingabe == ""):
            break
        s.sendall(eingabe.encode("UTF8"))
        bytes = s.recv(1024)
        print("Response from server:", bytes.decode("UTF8")) #decode and output received data
        if (eingabe == "quit"): 
            s.close()


