import pygame
import sys
import os
import subprocess 
from accueil import *
from avance import *
from jeux import *
from fight import *
from boutique import *
from pokedex import *
from inventaire import *
from boutique import *
from player1 import *

pygame.init()

clock = pygame.time.Clock()
size = width, height = 1500, 1000

screen = pygame.display.set_mode(size)

Avancement = avance()
lancement = accueil(screen,Avancement)
player = joueur()
game = jeux(screen,Avancement,player)



affpokedex = pokedex(player,screen,Avancement)


while True:

    while Avancement.get_lancement() :
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        lancement.main()
      
    
    while Avancement.get_host() :
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()


    while Avancement.get_player() :
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        
        joueurlan = player1(screen)
        joueurlan.main()


    while Avancement.get_lancement()!= True and Avancement.get_jeux() and Avancement.get_combat() != True and Avancement.get_pokedex() == False and Avancement.get_sac() == False and Avancement.get_shop() == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        game.main()

    while Avancement.get_combat() == True :
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        combat = fight(screen,Avancement,player,game)
        combat.main()

    while Avancement.get_pokedex() == True :
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        affpokedex = pokedex(player,screen,Avancement)
        affpokedex.main()

    while Avancement.get_sac() == True :
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        sac = inventaire(screen,Avancement,player)
        sac.main()  

    while Avancement.get_shop() == True :
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        shop = boutique(screen,Avancement,player)
        shop.main() 
