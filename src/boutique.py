import pygame
from pygame.locals import *
import sys
from avance import *

class boutique():

    def __init__(self, screen, Avancement, player):
        self.fond = pygame.image.load("./resources/boutique/shop_pokemon.jpg")
        self.fond = pygame.transform.scale(self.fond, (1500, 1000))
        self.pokeball = pygame.image.load("./resources/boutique/pokeball.png")
        self.superball = pygame.image.load("./resources/boutique/superball.png")
        self.hyperball = pygame.image.load("./resources/boutique/hyperball.png")
        self.etat = True
        self.joueur = joueur
        # url = ("https://pokeapi.co/api/v2/pokemon/"+nom+"/")
        # self.r = requests.get(url)
        # self.jsonfile = self.r.json()

        self.avancement = Avancement
        self.screen = screen

    def main(self):
        self.blitbase()

    def blitbase(self):
        self.screen.blit(self.fond, (0, 0))
        self.screen.blit(self.pokeball, (730, 160))
        self.screen.blit(self.superball, (1025, 160))
        self.screen.blit(self.hyperball, (1305, 160))
        pygame.display.flip()

    def quitter(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()


