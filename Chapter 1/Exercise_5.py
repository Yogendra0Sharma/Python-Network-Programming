#Author : Yogendra Sharma
#Date   : 28/06/2017

# map a protocol name (e.g. 'tcp') to a number

# importing python socket module
import socket


PORT = socket.getprotobyname("tcp")
print("{0} ".format(PORT))
