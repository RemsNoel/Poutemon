# import the pygame module, so you can use it
import pygame
import sys

# initialize the pygame module
pygame.init()
# Init the clock
clock = pygame.time.Clock()

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0) # Pas très joli mais c'est pas grave les amis
BLUE = (0, 0, 128) # Celui non plus mais on fait du mieux qu'on peut
CIEL = (0, 200, 255)
RED = (255, 0, 0)
ORANGE = (255, 100, 0)

# size
SCREEN_WIDTH = 750
SCREEN_HEIGHT = 596

# define a variable to control the main loop


class Game:
    # initialize
    def __init__(self):
        # set the size of the screen
        self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

        # load and set the logo
        logo = pygame.image.load("icone_app.png")
        pygame.display.set_icon(logo)
        pygame.display.set_caption("Poutemon")

        self.create_bg()
        

    # for the background
    def create_bg(self):
        self.bg1 = pygame.image.load("bg1.png")

    # for the text part
    def make_text(self, message, size, color):
        self.screen_rect = self.screen.get_rect()  
        font = pygame.font.SysFont('Arial', size)
        text = font.render(message,True,color)
        rect = text.get_rect(center = (self.screen_rect.centerx, self.screen_rect.centery) )
        return text,rect

    def update_textes(self):
        self.textes = ['Je vais te goumer.', 
        'Tva voir.', 
        'rira bien qui rira le dernier.', 
        'arrête de cliquer.', 
        'ça va mal se passer.']

    def main(self):
        done = False
        #Bg image
        self.screen.blit(self.bg1, (0, 0))
        pygame.display.flip()

        self.update_textes()
        pygame_text = []
        for text in self.textes:
            pygame_text.append(self.make_text(text, 24, BLUE))
        text,rect = pygame_text[0]#set a default
        

        #Display an image
        image = pygame.image.load("angry.png")
        image1 = pygame.image.load("chut.png")
        dialogue = pygame.image.load("dialogue.png")

        i = 0; # variable pour avancer dans le dialogue (ou tout simplement dans le jeu)
        imin = 0; # On commence à 0
        imax = len(self.textes) - 1; # on prend le nombre de dialogues stockés dans possible_outcome, on fera plusieurs variables dans ce style je pense afin de naviguer dans le jeu

        # main loop
        while not done:
            # event handling, gets all event from the event queue
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if i < imax:
                        i = i + 1
                    text,rect = pygame_text[i]
                    print(imax)
                    print(i)

                # # define the position of the smiley
                xpos = 29
                ypos = 50

                self.screen.blit(image1, (-15, -250))
                self.screen.blit(image, (xpos, ypos))
                self.screen.blit(dialogue, (-102, 410))
                self.screen.blit(text, [40, 486])
                pygame.display.flip()
            
                clock.tick(60)

                # # only do something if the event is of type QUIT
                # if event.type == pygame.QUIT:
                #     # change the value to False, to exit the main loop
                #     running = False
                if i == imax :
                    done = True
    
    def gamequit():
        print("Quit")
        pygame.quit()
        sys.exit()

     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    game = Game()
    game.main()