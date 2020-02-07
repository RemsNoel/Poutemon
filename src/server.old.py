import socket
import pygame
from fight import *


class server():

    def __init__(self):
        self.host = "127.0.0.1"
        self.port = 8080

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.host, self.port))
        self.sock.listen(1)

    def main(self):
        while True:
            print('Listen on localhost:8080')
            (self.sockClient, self.addrClient) = self.sock.accept()
            print("Client's address : ", self.addrClient)
            try:
                while True:
                    self.data = self.sockClient.recv(2048)
                    if self.data == '':
                        break
                    self.p = self.data.decode()
                    print(self.p)
                    if self.p == '':
                        break
                    self.p2 = self.p.split()
                    print(self.p2)
                    self.message = "lol"
                    self.sockClient.sendall(self.message.encode())
                self.sockClient.close()
            except socket.error:
                print('client interrompu')
        self.sock.close()



