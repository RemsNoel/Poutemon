import pygame
from pygame.locals import *
import sys

class avance():

    def  __init__(self):
        self.lancement = True
        self.jeux = True

    def get_lancement(self):
        return self.lancement
       
    def get_jeux(self):
        return self.jeux

    def set_lancement(self,etat):
        self.lancement = etat
        
    def set_jeux(self,etat):
        self.jeux = etat

    