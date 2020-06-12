import sys
import socket #Import socket module



s = socket.socket() #Create a socket Object 
host = '' #unspecified ip - all interfaces on host
port = 12345 #Reserve a port for your service



s.bind((host, port)) #Bind to the port


try: 
    s.listen(1) #Now wait for client connection 
    connection, client_address = s.accept() #Establish /get one connection with client
    while True:
        print('Got connection from %s' % str(client_address), file=sys.stderr)
        #Receive the data in small chunks and retransmit it

        byte_data = connection.recv(30) #read maximum of 30 bytes from connection
        data = byte_data.decode("latin1") #convert byte data to string
        print("received ""%s" % data, file=sys.stderr)
        print("sending data back to the client", file=sys.stderr)
        connection.sendall(("server got: %s"% data).encode("latin1")) #send reply to connection
    
except:
    print("Unexpected error: ", sys.exc_info()[0])
    
finally: 
    connection.close() #clean up the connection
    #s.close()  #clean up listening socket