import pygame
from pygame.locals import *
import sys
from avance import *
from zones import *
from pokemon import *
from joueur import *
from pokedex import *

class jeux ():

    def __init__(self,screen,Avancement,joueur):

        self.avancement = Avancement
        self.screen = screen

        self.zone2 = zones("./resources/zones_debut/maison_professeur.jpg","ville","","Sortir de la ville")
        self.zone1 = zones("./resources/zones_debut/maison_joueur.jpg","safe",self.zone2,"Aller vers la maison du professeur")
      
        self.joueur = joueur
        self.zone_actuel = self.zone1

        self.highlight = pygame.image.load("./resources/fond_ecran/highlight.png")
        self.fond = pygame.image.load("./resources/fond_ecran/blackscreen.png")
        

        
    def main(self):
        self.texte()

        if self.rect_sac.collidepoint(pygame.mouse.get_pos()):
            self.screen.blit(self.highlight, (50, 580))
            pygame.display.flip()

        elif self.rect_pokedex.collidepoint(pygame.mouse.get_pos()):
            self.screen.blit(self.highlight, (50, 680))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    self.avancement.set_pokedex(True)

        elif self.rect_quitter.collidepoint(pygame.mouse.get_pos()):    
            self.screen.blit(self.highlight, (50, 930))
            pygame.display.flip()

        elif self.rect_balade.collidepoint(pygame.mouse.get_pos()):    
            self.screen.blit(self.highlight, (340, 710))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN and event.button == 1:

                    if self.zone_actuel.get_typezone() == "safe":
                        
                        self.texte()
                        self.popupcombat = pygame.image.load("./resources/texte/nocombat.png")
                        self.screen.blit(self.popupcombat, (0,-100))
                        pygame.display.flip()
                        pygame.time.wait(1000)
                        self.texte()
                    else :
                        self.txt = self.font_obj.render('Tu te balades dans la zone ...', False, (255,255,255))
                        self.screen.blit(self.fond, (0, 0))
                        self.screen.blit(self.txt, (400, 800))
                        pygame.display.flip()
                        pygame.time.wait(2000)
                        self.avancement.set_combat(True)

        elif self.rect_zonesuivante.collidepoint(pygame.mouse.get_pos()):    
            self.screen.blit(self.highlight, (340, 780))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    
                    self.zone_actuel = self.zone_actuel.get_zonesuivante()


        else:   
            self.texte()

        
    def set_zone(self,zone):
        self.zone_actuel = zone

    def get_zone(self):
        return self.zone_actuel


    def blitbase(self):
        self.fond = pygame.image.load(self.zone_actuel.get_actuel())
        self.screen.blit(self.fond, (0, 0))
        

    def texte(self):

        self.blitbase()
        self.text = pygame.image.load("./resources/texte/text.png")
        self.screen.blit(self.text, (0, 0))

        self.font_obj = pygame.font.Font('./resources/font/Mermaid1001.ttf', 32)

        self.sac_texte =  self.font_obj.render('SAC', False, (255,255,255))
        self.rect_sac = self.sac_texte.get_rect()
        self.rect_sac.topleft = (130, 600)

        self.pokedex_texte =  self.font_obj.render('POKEDEX', False, (255,255,255))
        self.rect_pokedex = self.pokedex_texte.get_rect()
        self.rect_pokedex.topleft = (110, 700)

        self.quitter_texte =  self.font_obj.render('QUITTER', False, (255,255,255))
        self.rect_quitter = self.quitter_texte.get_rect()
        self.rect_quitter.topleft = (110, 950)

        self.balade_texte =  self.font_obj.render('Se promener dans la zone', False, (255,255,255))
        self.rect_balade = self.balade_texte.get_rect()
        self.rect_balade.topleft = (400, 730)

        self.zonesuivante_texte = self.font_obj.render(self.zone_actuel.get_txtzonesuivante(), False, (255,255,255))
        self.rect_zonesuivante = self.zonesuivante_texte.get_rect()
        self.rect_zonesuivante.topleft = (400, 800)

        self.screen.blit(self.sac_texte, (130, 600))
        self.screen.blit(self.pokedex_texte, (110, 700))
        self.screen.blit(self.quitter_texte, (110, 950))

        self.screen.blit(self.balade_texte, (400, 730))
        self.screen.blit(self.zonesuivante_texte, (400, 800))

        pygame.display.flip()

        






        
    

        
        
        





