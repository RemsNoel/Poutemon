import pygame
import sys

class joueur():

    def __init__(self):
        self.argent = 100
        self.objet = []
        self.pokemon = ["bulbasaur","eevee"]

    def get_pokemon(self):

        return self.pokemon

    
    def addpokemon(self,pokemon):
        if len(self.pokemon) < 6:
            self.pokemon.append(pokemon.get_name())
            print (self.pokemon)
        


       





