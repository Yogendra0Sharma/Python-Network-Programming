#Author : Yogendra Sharma
#Date   : 28/06/2017

# Take port number from user and show service belong to given port.

# importing python socket module

import socket


def ShowServiceByPort(port):
    try:
    service = socket.getservbyport(port)
    print("The Port '{0}' Belongs to '{1}' Service".format(port,service))
    except OSError:
        print("Oops!  That was no valid number.  Try again...")

if __name__ == "__main__":
    port = int(input("enter a port number:"))
    ShowServiceByPort(port)
    
