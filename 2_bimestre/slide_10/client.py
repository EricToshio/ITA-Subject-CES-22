#!/usr/bin/env python

from socket import *
import threading

HOST = '127.0.0.1' # or 'localhost'
PORT = 21567
BUFSIZ = 1024
tcpCliSock = socket(AF_INET, SOCK_STREAM)
ADDR = (HOST, PORT)
tcpCliSock.connect(ADDR)
host=tcpCliSock.getsockname() # print client host name


def listen():
    while True:
        data = tcpCliSock.recv(BUFSIZ)

        if data:
            print(data.decode('utf-8'))


threading.Thread(target = listen).start()
while True:

    data = (input()).encode('utf-8')

    if data:
        tcpCliSock.send(data)
    
tcpCliSock.close()