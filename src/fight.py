from type import *
import pygame
import sys
import random
from pokemon import *
from capture import *
from joueur import *

class fight():

    def __init__(self,screen,Avancement,joueur,zone,game):
        self.avancement = Avancement
        self.screen = screen
        self.game = game
        self.fondbataille = pygame.image.load("./resources/bataille/fond_bataille.png")
        
        self.infocombat = pygame.image.load("./resources/texte/infocombat.png")
        self.text = pygame.image.load("./resources/texte/text.png")
        self.font_obj = pygame.font.Font('./resources/font/Mermaid1001.ttf', 32)
        self.highlight = pygame.image.load("./resources/fond_ecran/highlight.png")
        self.point = pygame.image.load("./resources/point.png")

        self.joueur = joueur
       
        self.zone = zone

        self.ennemi = self.adversaire(self.zone)
        self.pokesauvage = pokemon(self.ennemi)

        self.poke1 = self.joueur.get_pokemon(0)
        if self.poke1 != "":
            self.pokemon1 = pokemon(self.poke1)

        self.poke2 = self.joueur.get_pokemon(1)
        if self.poke2 != "":
            self.pokemon2 = pokemon(self.poke2)

        self.poke3 = self.joueur.get_pokemon(2)
        if self.poke3 != "":
            self.pokemon3 = pokemon(self.poke3)

        self.poke4 = self.joueur.get_pokemon(3)
        if self.poke4 != "":
            self.pokemon4 = pokemon(self.poke4)

        self.pokemonjoueur = self.pokemon1

        self.combatencours = True
        self.tour = True
    
    def main(self):

        while self.combatencours :
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
        
            self.blitbase()
            print (self.pokesauvage.get_hp())
            print (self.pokemonjoueur.get_hp())

            while self.tour == True:
                self.blitbase()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT: sys.exit()

                    
                    if event.type == MOUSEBUTTONDOWN and event.button == 1:
                        if self.rect_capture.collidepoint(pygame.mouse.get_pos()):

                            self.capture = capture(0.5,self.pokesauvage)
                            self.resultatcapture = self.capture.get_result()
                            print (self.resultatcapture)

                            if self.resultatcapture == True:
                                print ("le pokemon est capture")
                                self.joueur.addpokemon(self.pokesauvage)

                                self.tour = False
                                self.combatencours = False
                              
                                

                            if self.resultatcapture == False:
                                print ("le pokemon c'est enfui")
                                self.tour = False

                        if self.rect_attaque1.collidepoint(pygame.mouse.get_pos()):
                            self.screen.blit(self.point, (380, 800))
                            pygame.display.flip()

                            self.pokesauvage.set_hp(5)
                            print (self.pokesauvage.get_hp())
                            self.tour = False

                        if self.rect_attaque2.collidepoint(pygame.mouse.get_pos()):
                            self.screen.blit(self.point, (380, 800))
                            pygame.display.flip()

                            self.pokesauvage.set_hp(7)
                            print (self.pokesauvage.get_hp())
                            self.tour = False

                        if self.rect_attaque3.collidepoint(pygame.mouse.get_pos()):
                            self.screen.blit(self.point, (380, 800))
                            pygame.display.flip()

                            self.pokesauvage.set_hp(2)
                            print (self.pokesauvage.get_hp())
                            self.tour = False

                        if self.rect_attaque4.collidepoint(pygame.mouse.get_pos()):

                            self.screen.blit(self.point, (380, 800))
                            pygame.display.flip()

                            self.pokesauvage.set_hp(3)
                            print (self.pokesauvage.get_hp())
                            self.tour = False

            while self.tour == False:
                self.blitbase()
                self.pokemonjoueur.set_hp(4)
                print (self.pokemonjoueur.get_hp())
                self.tour = True

        self.avancement.set_combat(False)
        self.avancement.set_jeux(True)
        
              

    def blitbase(self):
        self.screen.blit(self.fondbataille, (0, 0))
        self.fondbataille = pygame.transform.scale(self.fondbataille, (1500, 1000))
        self.screen.blit(self.text, (0, 0))
        self.text = pygame.transform.scale(self.text, (1500, 1000))
        

        self.capture_texte =  self.font_obj.render('CAPTURE', False, (255,255,255))
        self.rect_capture = self.capture_texte.get_rect()
        self.rect_capture.topleft = (130, 600)

        self.attaque1 =  self.font_obj.render(self.pokemonjoueur.get_attaque(0), False, (255,255,255))
        self.rect_attaque1 = self.attaque1.get_rect()
        self.rect_attaque1.topleft = (400, 800)

        self.attaque2 =  self.font_obj.render(self.pokemonjoueur.get_attaque(1), False, (255,255,255))
        self.rect_attaque2 = self.attaque2.get_rect()
        self.rect_attaque2.topleft = (650, 800)

        self.attaque3 =  self.font_obj.render(self.pokemonjoueur.get_attaque(2), False, (255,255,255))
        self.rect_attaque3 = self.attaque3.get_rect()
        self.rect_attaque3.topleft = (400, 900)

        self.attaque4 =  self.font_obj.render(self.pokemonjoueur.get_attaque(3), False, (255,255,255))
        self.rect_attaque4 = self.attaque4.get_rect()
        self.rect_attaque4.topleft = (650, 900)

        self.hpps =  self.font_obj.render(str(self.pokemonjoueur.get_hp()), False, (255,255,255))
        self.hppj =  self.font_obj.render(str(self.pokesauvage.get_hp()), False, (255,255,255))

        self.screen.blit(self.hpps, (550, 600))
        self.screen.blit(self.hppj, (1000, 550))

        self.screen.blit(self.pokesauvage.get_front_sprite(), (1000, 500))
        self.screen.blit(self.pokemonjoueur.get_back_sprite(), (500, 600))
        

        self.screen.blit(self.capture_texte, (130, 600))

        self.screen.blit(self.attaque1, (400, 800))
        self.screen.blit(self.attaque2, (650, 800))
        self.screen.blit(self.attaque3, (400, 900))
        self.screen.blit(self.attaque4, (650, 900))

        pygame.display.flip()
 
    def adversaire(self,zone):
        self.adv = random.choice(zone.get_pool(zone.get_typezone()))
        return self.adv



    # methode qui permet d'appeler la methode d'attaque de la classe correspondante en fonction du type en entrée
    def attaque(self, typeattaque, typedefense, basededegat):
        type = Type()
        att = type.determiner(typeattaque)
        deff = type.determiner(typedefense)
        degat = basededegat * att.attaque(deff.name)
        return degat

    # methode qui permet d'appeler la methode defend de la classe correspondante en fonction du type en entrée
    def defend(self, typedefense, typeattaque, basededegat):
        type = Type()
        deff = type.determiner(typedefense)
        att = type.determiner(typeattaque)
        degat = basededegat * deff.defend(att.name)
        return degat

    
