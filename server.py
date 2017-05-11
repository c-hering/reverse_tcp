#!/usr/bin/python
import socket

s = socket.socket()
host = socket.gethostname()
port = 37531
s.bind((host,port))

def snapshot():
	fp = open('image.jpeg','w')
	while True:
		recv_string = c.recv(1024)
		if not recv_string:
			break
		fp.write(recv_string)
	fp.close()
	print "image recieved"

def checkstring():
	if send_string == "snapshot":
		snapshot()

s.listen(5)
c, addr = s.accept()
print('CONN', addr)
while True:
	send_string = raw_input("Type: ")
	c.send(send_string)
	checkstring()
	print c.recv(1024)
c.close()
