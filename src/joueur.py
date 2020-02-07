import pygame
import sys

class joueur():

    def __init__(self):
        self.argent = 1000
        self.objet = []
<<<<<<< HEAD
        self.pokemon = ["bulbasaur","eevee"]
=======
        self.pokemon = ["bulbasaur","","",""]
        self.items =  {}
        self.items["pokeball"] = 0
        self.items["superball"] = 0
        self.items["hyperball"] = 0
>>>>>>> 4c5e4f7ce65aad7a404d43e699f8a19c4a314507

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





