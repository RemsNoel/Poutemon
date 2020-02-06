import pygame
from pygame.locals import *
import sys
from avance import *

class boutique():

    def __init__(self, screen, Avancement):
        self.fond = pygame.image.load("./resources/boutique/shop_pokemon.jpg")
        self.fond = pygame.transform.scale(self.fond, (1500, 1000))
        self.pokeball = pygame.image.load("./resources/boutique/pokeball.png")
        self.etat = True

        self.avancement = Avancement
        self.screen = screen

    def main(self):
        self.blitbase()

    def blitbase(self):
        self.screen.blit(self.fond, (0, 0))
        self.screen.blit(self.pokeball, (45, 200))
        pygame.display.flip()

    def quitter(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()


