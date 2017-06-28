#Author : Yogendra Sharma
#Date   : 28/06/2017


#importing python socket module
import socket

local_host_name = socket.gethostname()
print("Local Machine Host Name: %s" % local_host_name)
