# Python program to get IP Address

import socket

hostname = socket.gethostname()

IPAddr = socket.gethostbyname(hostname)

AllInfo = socket.gethostbyaddr(hostname)

print("Your Computer's Name is: {}".format(hostname))

print("Your Computer IP Address is: {}".format(IPAddr))

#print(AllInfo)

print("Computer's Name: {}, IP Address: {}".format(AllInfo[0], AllInfo[2]))

# https://www.pythonforbeginners.com/code-snippets-source-code/python-socket-examples
# https://www.programcreek.com/python/example/2611/socket.gethostbyaddr
# https://programtalk.com/python-examples/socket.gethostbyaddr/