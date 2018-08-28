import socket

my_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
my_socket.connect(('data.pr4e.org',80))

my_socket.send(b'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\n\n')

while True:
	data = my_socket.recv(512)
	if ( len(data) < 1):
		break
	print(data)

my_socket.close()
