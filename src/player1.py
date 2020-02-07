import socket, os
import pygame
from pokemonmulti import *
import random

class player1():

    def __init__(self,screen):

        self.host = "127.0.0.1"
        self.port = 8080
        self.screen = screen

        self.fond = pygame.image.load("./resources/fond_ecran/blackscreen.png")
        self.equipe = []

        self.font_obj = pygame.font.Font('./resources/font/Mermaid1001.ttf', 32)
        self.font_obj20 = pygame.font.Font('./resources/font/Mermaid1001.ttf', 20)
        self.encours = True

    def main(self):

        self.creationequipe()
        self.affichage_equipe()

        self.client = str(os.getpid())
        print('Connexion du client n°' + self.client)

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))


        self.message = "acier roche 30"

        self.sock.sendall(self.message.encode())
        self.data = self.sock.recv(2048)
        print('Reçu : ', self.data.decode())

        self.sock.close()

        while self.encours:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()

                

    def creationequipe(self):
        for i in range(6):
            self.id = random.randint(1,150)
            url = ("https://pokeapi.co/api/v2/pokemon/"+str(self.id)+"/")
            self.r = requests.get(url)
            self.jsonfile = self.r.json()
            self.name = str(self.jsonfile["name"])
            self.addpokemon(self.name)
        

    def addpokemon(self,pokemon):
        if len(self.equipe) < 6:
            self.equipe.append(pokemon)
            print (self.equipe)

    def affichage_equipe(self):
        self.screen.blit(self.fond, (0,0))

        self.longueur = len(self.equipe)
        
        for i in range(self.longueur):

            self.pokem = pokemon(self.equipe[i])
            self.pokemontext = self.font_obj20.render(str(self.pokem.get_name()), False, (255,255,255))
            self.pokemonhp = self.font_obj20.render(str(self.pokem.get_hp()), False, (255,255,255))
            self.screen.blit(self.pokemontext, (460, 15+(i*170)))
            self.screen.blit(self.pokemonhp, (560, 15+(i*170)))

            for j in range (4):

                self.pokemontext = self.font_obj20.render(str(self.pokem.get_attaque(j)), False, (255,255,255))
                self.screen.blit(self.pokemontext, (470, 50+(i*170 + j*25)))
        
        pygame.display.flip()
            
