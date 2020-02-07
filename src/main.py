import pygame
import sys
from accueil import *
from avance import *
from jeux import *
from fight import *
from boutique import *
from pokedex import *



pygame.init()

clock = pygame.time.Clock()
size = width, height = 1500, 1000

screen = pygame.display.set_mode(size)

Avancement = avance()
lancement = accueil(screen,Avancement)
player = joueur()
game = jeux(screen,Avancement,player)


while True:

    while Avancement.get_lancement() :
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        lancement.main()

    while Avancement.get_lancement()!= True and Avancement.get_jeux() and Avancement.get_combat() != True and Avancement.get_pokedex() == False:
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
            
