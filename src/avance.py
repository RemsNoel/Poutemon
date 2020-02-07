import pygame
from pygame.locals import *
import sys

class avance():

    def  __init__(self):
        self.lancement = True
        self.jeux = True
        self.combat = False

    def get_lancement(self):
        return self.lancement
       
    def get_jeux(self):
        return self.jeux

    def get_combat(self):
        return self.combat

    def set_lancement(self,etat):
        self.lancement = etat
        
    def set_jeux(self,etat):
        self.jeux = etat

    def set_combat(self,etat):
        self.combat = etat

    