#!/usr/bin/python
import socket

s = socket.socket()
host = socket.gethostname()
port = 25565
s.bind((host,port))
s.listen(5)
c, addr = s.accept()
print('CONN', addr)
try:
	while True:
		send_string = raw_input(">> ")
		c.send(send_string)
		print c.recv(1024)
	c.close()
except Exception as e:
	c.close()
	print('Exiting')
