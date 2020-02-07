import pygame
from pygame.locals import *
import sys
from avance import *

class accueil ():

    def __init__(self,screen,Avancement):
        self.fond = pygame.image.load("./resources/fond_ecran/page_accueil.png")
        self.fond = pygame.transform.scale(self.fond, (1500, 1000))
        self.commencer = pygame.image.load("./resources/fond_ecran/commencer.png")
        self.highlight = pygame.image.load("./resources/fond_ecran/highlight.png")
        
        
        self.avancement = Avancement
        self.screen = screen

    def main(self):
       
        self.blitbase()

        if self.rect_commencer.collidepoint(pygame.mouse.get_pos()):
            self.screen.blit(self.highlight, (10, 200))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    
                    self.avancement.set_lancement(False)
        else:
            self.blitbase()
        
    

    def blitbase(self):
        self.screen.blit(self.fond, (0, 0))
        self.screen.blit(self.commencer, (10, 200))
        self.rect_commencer = self.commencer.get_rect()
        self.rect_commencer.topleft=(10,200)
        pygame.display.flip()

    def quitter(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()

   
