import pygame
from pygame.locals import *
import sys
from avance import *

class boutique():

    def __init__(self, screen, Avancement):
        self.fond = pygame.image.load("./resources/fond_ecran/test.png")
        self.fond = pygame.transform.scale(self.fond, (1500, 1000))
        self.etat = True
        self.avancement = Avancement
        self.screen = screen

    def main(self):
        self.blitbase()

    def blitbase(self):
        self.screen.blit(self.fond, (0, 0))
        pygame.display.flip()

