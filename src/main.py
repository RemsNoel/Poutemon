# import the pygame module, so you can use it
import pygame
import sys
from accueil import *
from avance import *
from jeux import *
from fight import *

pygame.init()

clock = pygame.time.Clock()
size = width, height = 1500, 1000

screen = pygame.display.set_mode(size)

Avancement = avance()
print (Avancement.get_lancement())


lancement = accueil(screen,Avancement)
player = joueur()

game = jeux(screen,Avancement,player)

while Avancement.get_lancement() :
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    lancement.main()

while Avancement.get_lancement()!= True and Avancement.get_jeux() and Avancement.get_combat() != True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    
    game.main()

while Avancement.get_combat() == True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    combat = fight(screen,Avancement,player,game.get_zone(),game)
    combat.main()
    pygame.time.wait(10000)