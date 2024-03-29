import socket
import threading
import sys 
import argparse
from socket import *

#TODO: Implement all code for your server here
# python server.py -start -port 80 -passcode hi
# python3 server.py -start -port 1200 -passcode hi
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

sockets = []

def receive(socket):
	temp_username = ''
	while(True):
		message_with_flag = socket.recv(1024).decode()
		message = message_with_flag[:-1]
		flag = message_with_flag[-1:]
		sys.stdout.flush()
		if flag == "2":
			temp_username = message
			print(temp_username + " joined the chatroom")
			sys.stdout.flush()
			# print to all other clients
			for curr_connection_socket in sockets:
				if curr_connection_socket != socket:
					curr_connection_socket.send((temp_username + " joined the chatroom0").encode())
		elif flag == "3":
			print(message + " left the chatroom")
			sys.stdout.flush()
			sockets.remove(socket)
			for curr_connection_socket in sockets:
				if curr_connection_socket != socket:
					curr_connection_socket.send((message + " left the chatroom0").encode())
			socket.send("1".encode())
			socket.close()
			return
		else:
			print(message)
			sys.stdout.flush()
			for curr_connection_socket in sockets:
				curr_connection_socket.send((message+"0").encode())

# running server
while(True):
	connection_socket, addr = server_socket.accept()
	message_with_flag = connection_socket.recv(1024).decode()
	message = message_with_flag[:-1]
	flag = message_with_flag[-1:]
	if flag == "1":
		if message != PASSCODE:
			connection_socket.send("Incorrect passcode".encode())
			connection_socket.close()
		else:
			connection_socket.send("Correct passcode".encode())
			thread = threading.Thread(target=receive, args=(connection_socket,))
			thread.start()
			sockets.append(connection_socket)
			

			

	

# Use sys.stdout.flush() after print statemtents

if __name__ == "__main__":
	pass