#Author : Yogendra Sharma
#Date   : 28/06/2017


#importing python socket module
import socket

url = "www.github.com"
#get host ip by host name
remote_host_ip = socket.gethostbyname(url)
print("Github IP Address: %s" % remote_host_ip)
