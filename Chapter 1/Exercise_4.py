#Author : Yogendra Sharma
#Date   : 28/06/2017

# Get fully qualified domain name (FQDN) for remote host

# importing python socket module
import socket


REMOTE_HOST = "www.google.com"

FQDN = socket.getfqdn(REMOTE_HOST)

print("Fully qualified domain name(FQDN) of remote host {0} is {1} ".format(REMOTE_HOST ,FQDN))
