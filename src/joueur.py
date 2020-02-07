import pygame
import sys

class joueur():

    def __init__(self):
        self.argent = 1000
        self.objet = []
        self.pokemon = ["bulbasaur","","",""]
        self.items =  {}
        self.items["pokeball"] = 0
        self.items["superball"] = 0
        self.items["hyperball"] = 0

    def get_pokemon(self,i):

        return self.pokemon[i]
    
    def addpokemon(self,pokemon):
        for i in range(3):
            if self.pokemon[i] == "":
                self.pokemon[i].replace(self.pokemon[i],pokemon.get_name())

    def get_argent(self):
        return self.argent

    def get_items(self):
        return self.items





