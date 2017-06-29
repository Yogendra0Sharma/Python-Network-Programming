# Author : Yogendra Sharma
# Date   : 29/06/2017

# Socket Introduction and API
'''
1. Create a socket object
    s = socket.socket (socket_family, socket_type, protocol=0)

    socket_family: This is either AF_UNIX or AF_INET.

    socket_type: This is either SOCK_STREAM or SOCK_DGRAM.

    protocol: This is usually left out, defaulting to 0.

2. Client Socket Methods
    Method	 Description
    
    s.connect()	This method actively initiates TCP server connection.
  
'''

import socket

# Create a Client socket
clientSocket = socket.socket()

# get the local host address
host = socket.gethostname()

# define port for this socket
port = 12345

# connect to server Socket using host and port
clientSocket.connect((host,port))

# send data to server
clientSocket.send(b"Hello World!")
# recive data from server to client, specify buffer size (i.e 1024)
data = clientSocket.recv(1024)
print("Echo data from server {0}".format(data))
clientSocket.close()
