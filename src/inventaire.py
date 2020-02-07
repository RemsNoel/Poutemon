import pygame
from pygame.locals import *
import sys
from avance import *
from objets import *

class inventaire():
    
    def __init__(self, screen, Avancement, joueur):
        # Images
        self.fond = pygame.image.load("./resources/inventaire.jpg")
        self.fond = pygame.transform.scale(self.fond, (1500, 1000))
        self.pokeball_img = pygame.image.load("./resources/boutique/pokeball.png")
        self.superball_img = pygame.image.load("./resources/boutique/superball.png")
        self.hyperball_img = pygame.image.load("./resources/boutique/hyperball.png")
        self.pokepiece_img = pygame.image.load('./resources/boutique/pokepiece.png')
        self.font_obj = pygame.font.Font('./resources/font/Mermaid1001.ttf', 32)

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

    def blitbase(self):
        self.screen.blit(self.fond, (0, 0))

        # Pokeball
        self.screen.blit(self.pokeball_img, (300, 100))
        self.crossSign = self.font_obj.render("x", False, (255,255,255))
        self.screen.blit(self.crossSign, (400, 130))
        self.superballNb = self.font_obj.render(str(self.itemsSuperball), False, (255,255,255))
        self.screen.blit(self.superballNb, (420, 130))

        # Superball
        self.screen.blit(self.superball_img, (302, 200))
        self.crossSign = self.font_obj.render("x", False, (255,255,255))
        self.screen.blit(self.crossSign, (402, 230))
        self.superballNb = self.font_obj.render(str(self.itemsSuperball), False, (255,255,255))
        self.screen.blit(self.superballNb, (422, 230))
        
        # Hyperball
        self.screen.blit(self.hyperball_img, (302, 300))
        self.crossSign = self.font_obj.render("x", False, (255,255,255))
        self.screen.blit(self.crossSign, (402, 330))
        self.hyperballNb = self.font_obj.render(str(self.itemsHyperball), False, (255,255,255))
        self.screen.blit(self.hyperballNb, (422, 330))

        # Infos Joueur
        self.argentJoueur = self.font_obj.render(str(self.argent), False, (255,255,255))
        self.screen.blit(self.pokepiece_img, (10,18))
        self.screen.blit(self.argentJoueur, (29,10))

        pygame.display.flip()


