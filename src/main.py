# import the pygame module, so you can use it
import pygame
import sys
from accueil import *
from avance import *

pygame.init()
# initialize the pygame module

# Init the clock
clock = pygame.time.Clock()
size = width, height = 1500, 1000

screen = pygame.display.set_mode(size)

Avancement = avance()
print (Avancement.get_lancement())

while Avancement.get_lancement() :
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    lancement = accueil(screen,Avancement)
    lancement.main()

while Avancement.get_lancement()!= True and Avancement.get_jeux() :
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    fond = pygame.image.load("./resources/fond_ecran/blackscreen.png")
    screen.blit(fond, (0, 0))
    pygame.display.flip()
