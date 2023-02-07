import socket
import threading
import sys 
import argparse
from socket import *

#TODO: Implement all code for your server here

# parsing command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('-start', action='store_true')
parser.add_argument('-port')
parser.add_argument('-passcode')
args = parser.parse_args()
start, server_port, PASSCODE = args.start, args.port, args.passcode

# initializing server socket
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(("127.0.0.1", int(server_port)))
server_socket.listen(1)
print("Server started on port " + server_port + ". Accepting connections")
sys.stdout.flush()

# running server
connection_socket, addr = server_socket.accept()
while(True):
	message_with_flag = connection_socket.recv(1024).decode()
	message = message_with_flag[:-1]
	flag = message_with_flag[-1:]
	if flag == "1":
		if message != PASSCODE:
			connection_socket.send("Incorrect passcode".encode())
			connection_socket.close()
		else:
			connection_socket.send("Correct passcode".encode())
	elif flag == "2":
		print(message + " joined the chatroom")
		sys.stdout.flush()
			

			

	

# Use sys.stdout.flush() after print statemtents

if __name__ == "__main__":
	pass