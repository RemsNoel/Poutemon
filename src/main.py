# import the pygame module, so you can use it
import pygame
 
# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()

    # colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREEN = (0, 255, 0) # Pas très joli mais c'est pas grave les amis
    BLUE = (0, 0, 128) # Celui non plus mais on fait du mieux qu'on peut

    # create a surface on screen that has the size of 1280 x 720
    screen_width = 750
    screen_height = 596
    
    screen = pygame.display.set_mode((screen_width,screen_height))
    screen_rect = screen.get_rect()

    
    # load and set the logo
    logo = pygame.image.load("droleabeille.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Poutemon")
    
    # cursor
    pygame.mouse.set_cursor(*pygame.cursors.tri_right)
     

    #Bg image
    bg1 = pygame.image.load("bg1.png")
    screen.blit(bg1, (0, 0))
    pygame.display.flip()
     
    # define a variable to control the main loop
    running = True

    done = False
    clock = pygame.time.Clock()

    # class for the text part
    def make_text(message, size, color):
        font = pygame.font.SysFont('Arial', size)
        text = font.render(message,True,color)
        rect = text.get_rect(center = (screen_rect.centerx, screen_rect.centery) )
        return text,rect
    
    pygame_text = []
    possible_outcome = ['Je vais te goumer.', 'Tva voir.', 'rira bien qui rira le dernier.', 'arrête de cliquer.', 'ça va mal se passer.']
    for outcome in possible_outcome:
        pygame_text.append(make_text(outcome, 24, BLUE))
    text,rect = pygame_text[0]#set a default

    #Display an image
    image = pygame.image.load("angry.png")
    image1 = pygame.image.load("chut.png")
    dialogue = pygame.image.load("dialogue.png")
    i = 0; # variable pour avancer dans le dialogue (ou tout simplement dans le jeu)
    imin = 0;
    imax = len(possible_outcome) - 1;

    

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

            screen.blit(image1, (-15, -250))
            screen.blit(image, (xpos, ypos))
            screen.blit(dialogue, (-102, 410))
            screen.blit(text, [40, 486])
            pygame.display.flip()
        
            clock.tick(60)

            # # only do something if the event is of type QUIT
            # if event.type == pygame.QUIT:
            #     # change the value to False, to exit the main loop
            #     running = False

    screen.blit(bg1, (0, 0))
    pygame.display.flip()
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()