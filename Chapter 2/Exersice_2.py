# Author : Yogendra Sharma
# Date   : 29/06/2017

# Socket Introduction and API
'''
1. Create a socket object
    s = socket.socket (socket_family, socket_type, protocol=0)

    socket_family: This is either AF_UNIX or AF_INET.

    socket_type: This is either SOCK_STREAM or SOCK_DGRAM.

    protocol: This is usually left out, defaulting to 0.

2. Server Socket Methods
    Method	 Description
    
    s.bind()	 This method binds address (hostname, port number pair) to socket.
    s.listen()	 This method sets up and start TCP listener.
    s.accept()	 This passively accept TCP client connection, waiting until connection arrives (blocking).
'''

import socket

# Create a server socket
serverSocket = socket.socket()

# get the local host address
host = socket.gethostname()

# define port for this socket
port = 12345

# bind the socket to host & port, so this socket can listening on a specific host on a specific port.
serverSocket.bind((host,port))

# serverSocket now wait for client connection, we can specify how many client can communicate.
serverSocket.listen(5)      # 5 client can connect.

# run for client connection
while 1:
    # Establish connection with client.
    clientSocket,clientaddress = serverSocket.accept()
    print("Got Connected with {0}".format(clientaddress))

    # Send some data to clinet socket.
    # Python 3.x all Strings are unicode so need to send byte string
    clientSocket.send(b"Thanks for connecting")
    clientSocket.close()
    
