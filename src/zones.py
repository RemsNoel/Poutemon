import pygame
import sys
class zones():

    def __init__(self,actuel,typezone,zone_suivante,txtzonesuivante):

        self.actuel = actuel
        self.typezone = typezone
        self.txtzonesuivante = txtzonesuivante
        self.zonesuivante = zone_suivante
      

    def get_actuel(self):
        return self.actuel

    def get_typezone(self):
        return self.typezone

    def get_txtzonesuivante(self):
        return self.txtzonesuivante

    def get_zonesuivante(self):
        return self.zonesuivante

    def set_actuel(self,zone):
        self.actuel = zone

    def get_pool(self,zone):
        self.pool = []
        if zone == "ville":
            self.pool = ["rattata","pikachu","meowth","tangela","eevee","jigglypuff","clefairy"]
        return self.pool


    


              