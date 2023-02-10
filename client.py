import socket
import threading
import sys 
import argparse
from socket import *
import datetime


#TODO: Implement a client that connects to your server to chat with other clients here
# python client.py -join -host 127.0.0.1 -port 80 -username andrew -passcode hi
# python3 client.py -join -host 127.0.0.1 -port 1200 -username andrew -passcode hi
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
	while(True):
		message_with_flag = socket.recv(1024).decode()
		message = message_with_flag[:-1]
		flag = message_with_flag[-1:]
		if flag == "0":
			print(message)
			sys.stdout.flush()
		else:
			return
	
def chat(socket, username):
	while(True):
		message = input()
		sys.stdout.flush()
		if message == ":)":
			socket.send((username + ": [feeling happy]" + "0").encode())
		elif message == ":(":
			socket.send((username + ": [feeling sad]" + "0").encode())
		elif message == ":mytime":
			time = datetime.datetime.now()
			socket.send((username + ": " + (time.strftime("%a %b %d %H:%M:%S %Y") + "0")).encode())
		elif message == ":+1hr":
			time = datetime.datetime.now() + datetime.timedelta(hours=1)
			socket.send((username + ": " + (time.strftime("%a %b %d %H:%M:%S %Y") + "0")).encode())
		elif message == ":Exit":
			socket.send((username + "3").encode())
			return			
		else:
			socket.send((username + ": " + message + "0").encode())

# intializing client socket and establishing connection
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((server_ip, int(server_port)))
client_socket.send((PASSCODE+"1").encode())
connection_status = client_socket.recv(1024).decode()
if connection_status == "Incorrect passcode":
	print("Incorrect passcode")
	sys.stdout.flush()
else:
	connected = 1
	print("Connected to " + server_ip + " on port " + server_port)
	sys.stdout.flush()
	client_socket.send((username+"2").encode())
	rthread = threading.Thread(target=receive, args=(client_socket,))
	cthread = threading.Thread(target=chat, args=(client_socket, username,))
	rthread.start()
	cthread.start()

# Use sys.stdout.flush() after print statemtents

if __name__ == "__main__":
	pass