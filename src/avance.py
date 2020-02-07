import pygame
from pygame.locals import *
import sys

class avance():

    def  __init__(self):
        self.lancement = True
        self.jeux = True
        self.combat = False
        self.pokedex = False
        self.sac = False
        self.shop = False
        self.host = False
        self.player = False

    def get_lancement(self):
        return self.lancement
       
    def get_jeux(self):
        return self.jeux

    def get_combat(self):
        return self.combat

    def get_pokedex(self):
        return self.pokedex
    
    def get_sac(self):
        return self.sac

    def get_shop(self):
        return self.shop

    def get_host(self):
        return self.host

    def get_player(self):
        return self.player

    def set_lancement(self,etat):
        self.lancement = etat
        
    def set_jeux(self,etat):
        self.jeux = etat

    def set_combat(self,etat):
        self.combat = etat

    def set_pokedex(self,etat):
        self.pokedex = etat

    def set_sac(self,etat):
        self.sac = etat

    def set_shop(self,etat):
        self.shop = etat

    def set_host(self,etat):
        self.host = etat

    def set_player(self,etat):
        self.player = etat
    