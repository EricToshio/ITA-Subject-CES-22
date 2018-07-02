import socket

import threading

from time import ctime

class ThreadedServer(object):
    
    def __init__(self, host, port):
        self.clients = []
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self):
        self.sock.listen(5)
        while True:
            client, address = self.sock.accept()
            self.clients.append(client)
            client.settimeout(60)
            threading.Thread(target = self.listenToClient,args = (client,address)).start()


    def listenToClient(self, client, address):
        name=""
        first_message = True
        size = 1024
        client.send(("Bem vindo ao chat!!! Por favor insira seu nome:").encode('utf-8'))
        while True:
            try:
                data = client.recv(size)
                if data:
                # Set the response to echo back the recieved data
                    strdata=data.decode('utf-8')
                    if first_message:
                        name=strdata
                        for every_client in self.clients:
                            every_client.send(('['+ctime()+'] '+name+", has just joined the chat!").encode('utf-8'))
                        print('['+ctime()+'] '+name+", has just joined the chat!")
                        first_message= False
                    else:
                        for every_client in self.clients:
                            every_client.send(('['+ctime()+'] '+name+': '+strdata).encode('utf-8'))
                        print('['+ctime()+'] '+name+': '+strdata)
                else:
                    raise error('Client disconnected')

            except:
                client.close()
                print("Exception")
                return False


if __name__ == "__main__":
    ThreadedServer('127.0.0.1',21567).listen()