import pygame
import sys

class joueur():

    def __init__(self):
        self.argent = 1000
        self.objet = []
        self.pokemon = ["bulbasaur"]
        self.items =  {}
        self.items["pokeball"] = 0
        self.items["superball"] = 0
        self.items["hyperball"] = 0

    def get_pokemon(self):

        return self.pokemon

    
    def addpokemon(self,pokemon):
        if len(self.pokemon) < 6:
            self.pokemon.append(pokemon.get_name())
            print (self.pokemon)
        

    def get_argent(self):
        return self.argent

    def get_items(self):
        return self.items

    def set_argentmoins(self, argent):
        self.argent = argent

    def set_pokeball(self, nb):
        self.items["pokeball"] = nb

    def set_superball(self, nb):
        self.items["superball"] = nb

    def set_hyperball(self, nb):
        self.items["hyperball"] = nb





