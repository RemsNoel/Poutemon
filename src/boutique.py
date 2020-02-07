import pygame
from pygame.locals import *
import sys
from avance import *
from objets import *

class boutique():

    def __init__(self, screen, Avancement, joueur):
        self.fond = pygame.image.load("./resources/boutique/shop_pokemon.jpg")
        self.fond = pygame.transform.scale(self.fond, (1500, 1000))
        self.pokeball_img = pygame.image.load("./resources/boutique/pokeball.png")
        self.superball_img = pygame.image.load("./resources/boutique/superball.png")
        self.hyperball_img = pygame.image.load("./resources/boutique/hyperball.png")
        self.pokepiece_img = pygame.image.load('./resources/boutique/pokepiece.png')
        self.font_obj = pygame.font.Font('./resources/font/Mermaid1001.ttf', 32)

        # API - Récupération du cost
        self.pokeball = "poke-ball"
        self.pokeballObj = objets(self.pokeball,1)
        self.pokeballCost = self.pokeballObj.get_cost()
        self.superball = "great-ball"
        self.superballObj = objets(self.superball,0.7)
        self.superballCost = self.superballObj.get_cost()
        self.hyperball = "ultra-ball"
        self.hyperballObj = objets(self.hyperball,0.2)
        self.hyperballCost = self.hyperballObj.get_cost()

        self.etat = True
        self.joueur = joueur
        self.argent = self.joueur.get_argent()
        self.items = self.joueur.get_items()
        self.itemsPokeball = self.items.get("pokeball")
        self.itemsSuperball = self.items.get("superball")
        self.itemsHyperball = self.items.get("hyperball")

        self.avancement = Avancement
        self.screen = screen


    def main(self):
        self.blitbase()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if self.rect_pokeball.collidepoint(pygame.mouse.get_pos()):
                    if self.argent >= self.pokeballCost:
                        self.argent = self.argent - self.pokeballCost
                        self.joueur.set_argentmoins(self.argent)
                        print (self.joueur.get_argent())
                        self.itemsPokeball += 1
                        print(self.itemsPokeball)
                        self.joueur.set_pokeball(self.itemsPokeball)

                elif self.rect_superball.collidepoint(pygame.mouse.get_pos()):
                    if self.argent >= self.superballCost:
                        self.argent = self.argent - self.superballCost
                        self.joueur.set_argentmoins(self.argent)
                        print (self.joueur.get_argent())
                        self.itemsSuperball += 1
                        self.joueur.set_superball(self.itemsSuperball)
                        
                elif self.rect_hyperball.collidepoint(pygame.mouse.get_pos()):
                    if self.argent >= self.hyperballCost:
                        self.argent = self.argent - self.hyperballCost
                        self.joueur.set_argentmoins(self.argent)
                        self.itemsHyperball += 1
                        self.joueur.set_hyperball(self.itemsHyperball)
                elif self.rect_quitter.collidepoint(pygame.mouse.get_pos()):
                    print(self.joueur.get_items().get("pokeball"))
                    self.avancement.set_shop(False)

    def blitbase(self):
        self.screen.blit(self.fond, (0, 0))

        #Img Pokeball + rect
        self.screen.blit(self.pokeball_img, (730, 160))
        self.rect_pokeball = self.pokeball_img.get_rect()
        self.rect_pokeball.topleft = (730,160)

        #Img Superball + rect
        self.screen.blit(self.superball_img, (1025, 160))
        self.rect_superball = self.superball_img.get_rect()
        self.rect_superball.topleft = (1025,160)

        #Img Hyperball + rect
        self.screen.blit(self.hyperball_img, (1305, 160))
        self.rect_hyperball = self.hyperball_img.get_rect()
        self.rect_hyperball.topleft = (1305,160)

        #Argent du joueur
        self.argentJoueur = self.font_obj.render(str(self.argent), False, (255,255,255))
        self.screen.blit(self.pokepiece_img, (1390,18))
        self.screen.blit(self.argentJoueur, (1410,10))
        
        # Affichage venant de l'api
        # Pokeball
        self.pokeballCostStr = self.font_obj.render(str(self.pokeballCost), False, (255,255,255))
        self.screen.blit(self.pokeballCostStr, (755,255))
        self.screen.blit(self.pokepiece_img, (810,261))
        self.crossSign = self.font_obj.render("x", False, (255,255,255))
        self.screen.blit(self.crossSign, (843, 195))
        self.pokeballNb = self.font_obj.render(str(self.itemsPokeball), False, (255,255,255))
        self.screen.blit(self.pokeballNb, (860, 196))

        # Superball
        self.superballCostStr = self.font_obj.render(str(self.superballCost), False, (255,255,255))
        self.screen.blit(self.superballCostStr, (1050,255))
        self.screen.blit(self.pokepiece_img, (1105,261))
        self.crossSign = self.font_obj.render("x", False, (255,255,255))
        self.screen.blit(self.crossSign, (1138, 195))
        self.superballNb = self.font_obj.render(str(self.itemsSuperball), False, (255,255,255))
        self.screen.blit(self.superballNb, (1155, 196))

        # Hyperball
        self.hyperballCostStr = self.font_obj.render(str(self.hyperballCost), False, (255,255,255))
        self.screen.blit(self.hyperballCostStr, (1330,255))
        self.screen.blit(self.pokepiece_img, (1385,261))
        self.crossSign = self.font_obj.render("x", False, (255,255,255))
        self.screen.blit(self.crossSign, (1418, 195))
        self.hyperballNb = self.font_obj.render(str(self.itemsHyperball), False, (255,255,255))
        self.screen.blit(self.hyperballNb, (1435, 196))

        # Quitter
        self.buttonQuit = self.font_obj.render("Quitter", False, (255,255,255))
        self.screen.blit(self.buttonQuit, (1350, 930))
        self.rect_quitter = self.buttonQuit.get_rect()
        self.rect_quitter.topleft = (1350,930)

        pygame.display.flip()

    def quitter(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()


