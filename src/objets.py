import pygame
import requests
import json

class objets():
    def __init__(self, nom):
        url = ("https://pokeapi.co/api/v2/item/"+nom+"/")
        self.r = requests.get(url)
        self.jsonfile = self.r.json()
        self.cost = int(self.jsonfile["cost"])
<<<<<<< HEAD
    
=======
        self.rate = 0
>>>>>>> c5f075d70b5f608624719224c28a1ecb5a3c3cb1
        

    def get_cost(self):
        return self.cost

    def get_rate(self):
        return self.rate