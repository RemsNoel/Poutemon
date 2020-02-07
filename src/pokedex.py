import pygame
import sys
from joueur import *
from pokemon import *
from avance import *

class pokedex():

    def __init__(self,joueur,screen,avancement):

        self.player = joueur
        self.avancement= avancement
        self.screen = screen
        self.fond = pygame.image.load("./resources/pokedex/pokedex.png")
        self.encours = True
        self.font_obj = pygame.font.Font('./resources/font/Mermaid1001.ttf', 32)
        self.font_obj20 = pygame.font.Font('./resources/font/Mermaid1001.ttf', 20)

    def main(self):
        self.blitbase()

        while self.encours:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                    
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if self.rect_quitter.collidepoint(pygame.mouse.get_pos()):
                        self.encours = False
                        self.avancement.set_pokedex(False)


    def blitbase(self):
        self.screen.blit(self.fond, (0, 0))

        self.argent = self.font_obj.render(str(self.player.get_argent())+" pieces", True, (255,255,255))
        self.screen.blit(self.argent, (600, 150))


        self.quitter = self.font_obj.render("X", True, (255,255,255))
        self.screen.blit(self.quitter, (820, 100))
        self.rect_quitter = self.quitter.get_rect()
        self.rect_quitter.topleft = (820, 100)

        self.listepoke = self.player.get_pokemon()
        self.longueur = len(self.listepoke)
        
        for i in range(self.longueur):
            self.pokem = pokemon(self.listepoke[i])
            self.pokemontext = self.font_obj20.render(str(self.pokem.get_name()), False, (255,255,255))
            self.pokemonhp = self.font_obj20.render(str(self.pokem.get_hp()), False, (255,255,255))
            self.screen.blit(self.pokemontext, (570, 340+(i*80)))
            self.screen.blit(self.pokemonhp, (670, 340+(i*80)))


        pygame.display.flip()

