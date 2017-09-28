import socket
import select 
import threading
import time
import sys

ip_address1 = "10.128.94.141"
ip_address = "127.0.0.1"
BUFFER = 1024
PORT = 6001

def main():
	class Server:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

		connections = []

		def __init__(self):
			#try catch
			self.s.bind((ip_address, PORT))
			self.s.listen(1)
			print "Waiting for a connection"

		def handler(self, c, a):
			while True:
				data = c.recv(1024)
				for conn in self.connections:
					conn.send(data)
				if not data:
					break

		def run(self):
			while True:
				conn, address = self.s.accept()
				serverThread = threading.Thread(target=self.handler, args=(conn, address))
				serverThread.start()
				print "Connection established with " 
				self.connections.append(conn)
			



	class Client:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                
		s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

		def sendMessage(self):
			while True:
				self.s.send(bytes(raw_input(""), 'utf-8'))

		def __init__(self, address):			
			self.s.connect((address, PORT))
			self.s.send(raw_input(""))  
			print "created"
			clientThread = threading.Thread(target = self.sendMessage)
			clientThread.start()              

		def run(self):
			while True:
				print "here"
				message = self.s.recv(1024)
				if not message:
					break


				
	if(len(sys.argv)>1):
		client = Client(sys.argv[1])
	else:
		server = Server()
		server.run()



if __name__ == "__main__":
	main()






