# Author : Yogendra Sharma
# Date   : 28/06/2017

# Creating a Socket

import socket

# Create an INET,Streaming socket
serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# bind the socket to host and port
serverSocket.bind((socket.gethostname(),12345))
# listen 5 client requests
serverSocket.listen(5)

    
