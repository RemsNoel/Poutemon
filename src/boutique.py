import pygame
from pygame.locals import *
import sys
from avance import *
from objets import *

class boutique():

    def __init__(self, screen, Avancement, joueur):
        # Images
        self.fond = pygame.image.load("./resources/boutique/shop_pokemon.jpg")
        self.fond = pygame.transform.scale(self.fond, (1500, 1000))
        self.pokeball_img = pygame.image.load("./resources/boutique/pokeball.png")
        self.superball_img = pygame.image.load("./resources/boutique/superball.png")
        self.hyperball_img = pygame.image.load("./resources/boutique/hyperball.png")
        self.pokepiece_img = pygame.image.load('./resources/boutique/pokepiece.png')
        self.font_obj = pygame.font.Font('./resources/font/Mermaid1001.ttf', 32)

        # API - Récupération du cost
        self.pokeball = "poke-ball"
        self.pokeballObj = objets(self.pokeball)
        self.pokeballCost = self.pokeballObj.get_cost()
        self.superball = "great-ball"
        self.superballObj = objets(self.superball)
        self.superballCost = self.superballObj.get_cost()
        self.hyperball = "ultra-ball"
        self.hyperballObj = objets(self.hyperball)
        self.hyperballCost = self.hyperballObj.get_cost()

        self.etat = True
        self.joueur = joueur
        self.argent = self.joueur.get_argent()

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
                elif self.rect_superball.collidepoint(pygame.mouse.get_pos()):
                    if self.argent >= self.superballCost:
                        self.argent = self.argent - self.superballCost
                elif self.rect_hyperball.collidepoint(pygame.mouse.get_pos()):
                    if self.argent >= self.hyperballCost:
                        self.argent = self.argent - self.hyperballCost

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
        # Superball
        self.superballCostStr = self.font_obj.render(str(self.superballCost), False, (255,255,255))
        self.screen.blit(self.superballCostStr, (1050,255))
        self.screen.blit(self.pokepiece_img, (1105,261))
        # Hyperball
        self.hyperballCostStr = self.font_obj.render(str(self.hyperballCost), False, (255,255,255))
        self.screen.blit(self.hyperballCostStr, (1330,255))
        self.screen.blit(self.pokepiece_img, (1385,261))

        pygame.display.flip()

    def quitter(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()


