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
parser.add_argument('-username')
parser.add_argument('-passcode')
args = parser.parse_args()
join, server_ip, server_port, username, PASSCODE = args.join, args.host, args.port, args.username, args.passcode

def receive(socket):
	print(socket.recv(1024).decode())
	sys.stdout.flush()
	
def chat(socket):
	socket.send(input().encode())

# intializing client socket and establishing connection
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((server_ip, int(server_port)))
client_socket.send((PASSCODE+"1").encode())
connection_status = client_socket.recv(1024).decode()
if connection_status == "Incorrect passcode":
	print("Incorrect passcode")
else:
	connected = 1
	print("Connected to " + server_ip + " on port " + server_port)
	client_socket.send((username+"2").encode())
	rthread = threading.Thread(target=receive, args=(client_socket,))
	cthread = threading.Thread(target=chat, args=(client_socket,))
	rthread.start()
	cthread.start()

# Use sys.stdout.flush() after print statemtents

if __name__ == "__main__":
	pass