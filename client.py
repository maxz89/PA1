import socket
import threading
import sys 
import argparse
from socket import *


#TODO: Implement a client that connects to your server to chat with other clients here

# parsing command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('-join', action='store_true')
parser.add_argument('-host')
parser.add_argument('-port')
parser.add_argument('-passcode')
args = parser.parse_args()
join, server_ip, server_port, PASSCODE = args.join, args.host, args.port, args.passcode

# intializing client socket and establishing connection
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((server_ip, int(server_port)))
client_socket.send((PASSCODE+"1").encode())
connection_status = client_socket.recv(1024).decode()
if connection_status == "0":
	print("Incorrect passcode.")
else:
	connected = 1
	while(connected):
		# placeholder
		i = 0



# Use sys.stdout.flush() after print statemtents

if __name__ == "__main__":
	pass