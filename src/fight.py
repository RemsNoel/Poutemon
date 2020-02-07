from type import *
import pygame
import sys
import random
from pokemon import *
from capture import *
from joueur import *
from objets import *


class fight():

    def __init__(self,screen,Avancement,joueur,game):
        self.avancement = Avancement
        self.screen = screen
        self.game = game
        self.fondbataille = pygame.image.load("./resources/bataille/fond_bataille.png")
        
        self.infocombat = pygame.image.load("./resources/texte/infocombat.png")
        self.text = pygame.image.load("./resources/texte/text.png")
        self.font_obj = pygame.font.Font('./resources/font/Mermaid1001.ttf', 32)
        self.highlight = pygame.image.load("./resources/fond_ecran/highlight.png")
        self.captureE = pygame.image.load("./resources/texte/captureE.png")
        self.captureR = pygame.image.load("./resources/texte/captureR.png")

        self.defaite = pygame.image.load("./resources/texte/defaite.png")
        self.victoire = pygame.image.load("./resources/texte/victoire.png")


        self.joueur = joueur
       
        self.zone = self.game.get_zone()

        self.ennemi = self.adversaire(self.zone)
        self.pokesauvage = pokemon(self.ennemi)

        self.listpokejoueur = self.joueur.get_pokemon()
        print(self.listpokejoueur)
        self.pokemonjoueur = pokemon(self.listpokejoueur[0])
        self.pokejouable = len(self.listpokejoueur)
        self.pokejoue = 1
         

        self.combatencours = True
        self.tour = True
    
    def main(self):

        while self.combatencours :
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
        
            self.blitbase()
            print (self.pokesauvage.get_hp())
            print (self.pokemonjoueur.get_hp())

            while self.tour == True and self.combatencours == True:
                self.blitbase()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT: sys.exit()

                    
                    if event.type == MOUSEBUTTONDOWN and event.button == 1:
                        if self.rect_capture.collidepoint(pygame.mouse.get_pos()):

                            self.capture = capture(0.5,self.pokesauvage)
                            self.resultatcapture = self.capture.get_result()
                            print (self.resultatcapture)

                            if self.resultatcapture == True:
                                self.screen.blit(self.captureR, (0, -100))
                                pygame.display.flip()
                                pygame.time.wait(1000)
                                print ("le pokemon est capture")
                                self.items = self.joueur.get_items()
                                self.itemsPokeball = self.items.get("pokeball")
                                self.itemsPokeball -= 1
                                self.joueur.addpokemon(self.pokesauvage)
                                self.combatencours = False
                                self.tour = False
                                self.joueur.set_argentmoins(self.joueur.get_argent()+random.randint(15,20))
                                
                              
                            if self.resultatcapture == False:
                                self.screen.blit(self.captureE, (0, -100))
                                pygame.display.flip()
                                pygame.time.wait(1000)
                                print ("le pokemon s'est enfui")
                                self.tour = False

                        if self.rect_attaque1.collidepoint(pygame.mouse.get_pos()):
                       

                            self.pokesauvage.set_hp(5)
                            if self.pokesauvage.get_hp() <= 0:
                                self.screen.blit(self.victoire, (0, -100))
                                pygame.display.flip()
                                pygame.time.wait(1000)
                                self.joueur.set_argentmoins(self.joueur.get_argent()+random.randint(5,10))
                                self.combatencours = False
                                self.tour = False
                         
                                
                            else :
                                self.tour = False

                        if self.rect_attaque2.collidepoint(pygame.mouse.get_pos()):
                            self.pokesauvage.set_hp(40)
                            if self.pokesauvage.get_hp() <= 0:
                                self.screen.blit(self.victoire, (0, -100))
                                pygame.display.flip()
                                pygame.time.wait(1000)
                                self.joueur.set_argentmoins(self.joueur.get_argent()+random.randint(5,10))
                                self.combatencours = False
                                self.tour = False
                   
                            else :
                                self.tour = False

                        if self.rect_attaque3.collidepoint(pygame.mouse.get_pos()):
                            self.pokesauvage.set_hp(20)
                            if self.pokesauvage.get_hp() <= 0:
                                self.screen.blit(self.victoire, (0,-100))
                                pygame.display.flip()
                                pygame.time.wait(1000)
                                self.joueur.set_argentmoins(self.joueur.get_argent()+random.randint(5,10))
                                self.combatencours = False
                                self.tour = False
                                
                            else :
                                self.tour = False

                        if self.rect_attaque4.collidepoint(pygame.mouse.get_pos()):
                            self.pokesauvage.set_hp(3)
                            if self.pokesauvage.get_hp() <= 0:
                                self.screen.blit(self.victoire, (0, -100))
                                pygame.display.flip()
                                pygame.time.wait(1000)
                                self.joueur.set_argentmoins(self.joueur.get_argent()+random.randint(5,10))
                                self.combatencours = False
                                self.tour = False
                                
                            else :
                                self.tour = False

            while self.tour == False and self.combatencours == True:
                self.blitbase()
                pygame.time.wait(1000)

                self.pokemonjoueur.set_hp(10)

                
                if self.pokemonjoueur.get_hp() <= 0:
                    self.pokejoue += 1
                    print (self.pokejoue)
                    print (self.pokejouable)

                    if self.pokejoue < self.pokejouable:
                        self.pokemonjoueur = pokemon(self.listpokejoueur[self.pokejoue-1])
                        print (self.pokemonjoueur.get_name())
                        self.tour = True   
                            
                    else:
                        self.screen.blit(self.defaite, (0, -100))
                        pygame.display.flip()
                        self.joueur.set_argentmoins(self.joueur.get_argent()-random.randint(40,45))
                        pygame.time.wait(1000)
                        self.combatencours = False
                        self.tour = True
                        

                else :
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

    
