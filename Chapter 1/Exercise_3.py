#Author : Yogendra Sharma
#Date   : 28/06/2017

# Get a Host Name from given IP Address

#importing python socket module
import socket
IP = "127.0.0.1"
# get host name from IP address
host_name = socket.gethostbyaddr(IP)
print("IP {0} is resolved as Host Name {1}".format(IP ,host_name[0]))
