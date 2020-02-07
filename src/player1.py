import socket, os


class player1():

    def main(self):

        self.host = "127.0.0.1"
        self.port = 8080

        self.client = str(os.getpid())
        print('Connexion du client n°' + self.client)

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))


        self.message = "acier roche 30"

        self.sock.sendall(self.message.encode())
        self.data = self.sock.recv(2048)
        print('Reçu : ', self.data.decode())

        self.sock.close()