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

        if self.rect_host.collidepoint(pygame.mouse.get_pos()):
        
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    self.avancement.set_lancement(False)
                    self.avancement.set_host(True)
                    self.avancement.set_player(True)

        if self.rect_rejoindre.collidepoint(pygame.mouse.get_pos()):

            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    self.avancement.set_lancement(False)
                    self.avancement.set_player(True)
                    
        else:
            self.blitbase()
        
    

    def blitbase(self):

        self.font_obj = pygame.font.Font('./resources/font/Mermaid1001.ttf', 32)

        self.screen.blit(self.fond, (0, 0))
        self.screen.blit(self.commencer, (10, 200))
        self.rect_commencer = self.commencer.get_rect()
        self.rect_commencer.topleft=(10,200)

        self.host =  self.font_obj.render('Host', False, (255,255,255))
        self.screen.blit(self.host, (10, 350))
        self.rect_host = self.host.get_rect()
        self.rect_host.topleft = (10, 350)

        self.rejoindre =  self.font_obj.render('rejoindre', False, (255,255,255))
        self.screen.blit(self.rejoindre, (10, 400))
        self.rect_rejoindre = self.rejoindre.get_rect()
        self.rect_rejoindre.topleft = (10, 400)


        pygame.display.flip()

    def quitter(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()

   
