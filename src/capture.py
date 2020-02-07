import pygame
from pygame.locals import *
import sys


class capture():

    def __init__(self,ball,pokemon):
        self.balle = ball
        self.cible = pokemon
        self.result = False

    def main(self):
        self.r = self.cible.get_hp()*self.balle
        if self.r < 5:
            print (self.result)
            self.result = True
        else:
            print (self.result)
            self.result = False
    
    def get_result(self):
        self.main()
        print (self.result)
        return self.result




