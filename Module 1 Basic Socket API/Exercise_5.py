#Author : Yogendra Sharma
#Date   : 28/06/2017

# get port number from service name.

# importing python socket module

import socket
service = "ssh"
port = socket.getservbyname(service)
print("The Service '{0}' listing on '{1}' Port".format(service,port))
