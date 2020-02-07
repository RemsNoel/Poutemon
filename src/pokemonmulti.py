import pygame
import requests
import json

class pokemon():

    def __init__(self,nom):
        url = ("https://pokeapi.co/api/v2/pokemon/"+nom+"/")
        self.r = requests.get(url)
        self.jsonfile = self.r.json()

        self.hp = int(self.jsonfile["stats"][5]["base_stat"])
        self.name = str(self.jsonfile["name"])

        self.attaques = []
        
        for i in range(4):
            self.attaques.append(self.jsonfile["moves"][i]["move"]["name"])

    def get_hp(self):
        return self.hp

    def set_hp(self,hp):
        self.hp =  self.hp-hp

    def get_name(self):
        return self.name
    
    def get_attaque(self,i):
        return self.attaques[i]


    

