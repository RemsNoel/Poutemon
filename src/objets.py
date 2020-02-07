import pygame
import requests
import json

class objets():
    def __init__(self, nom):
        url = ("https://pokeapi.co/api/v2/item/"+nom+"/")
        self.r = requests.get(url)
        self.jsonfile = self.r.json()
        self.cost = int(self.jsonfile["cost"])
    
        

    def get_cost(self):
        return self.cost