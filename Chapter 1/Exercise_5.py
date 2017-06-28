#Author : Yogendra Sharma
#Date   : 28/06/2017

# get service name from port number.

# importing python socket module

import socket
port = 80
service = socket.getservbyport(port)
print("The Port {0} is represent \"{1}\" Service".format(port,service))
