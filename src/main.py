# import the pygame module, so you can use it
import pygame
 
# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    logo = pygame.image.load("droleabeille.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Poutemon")
    
    pygame.mouse.set_cursor(*pygame.cursors.tri_right)
     

    # create a surface on screen that has the size of 1280 x 720
    screen_width = 750;
    screen_height = 596;

    screen = pygame.display.set_mode((screen_width,screen_height))

    #Bg image
    bg1 = pygame.image.load("bg1.png")
    screen.blit(bg1, (0, 0))
    pygame.display.flip()
     
    # define a variable to control the main loop
    running = True
     
    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():

            white = (255, 255, 255) 
            green = (0, 255, 0) 
            blue = (0, 0, 128) 

            font = pygame.font.Font('freesansbold.ttf', 24) 
            text = font.render('Je...Je vais te goumer.', True, blue)

            #Display an image
            image = pygame.image.load("angry.png")
            image1 = pygame.image.load("chut.png")
            dialogue = pygame.image.load("dialogue.png")

            # define the position of the smiley
            xpos = 29
            ypos = 50

            # now blit the smiley on screen
            screen.blit(image1, (-15, -250))
            screen.blit(image, (xpos, ypos))
            screen.blit(dialogue, (-102, 410))
            screen.blit(text, (40, 486))
            # and update the screen (don't forget that!)
            pygame.display.flip()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and event.pos[0] < screen_width and event.pos[1] < screen_height:
                    text2 =  font.render('Ahah... jrigole', True, blue)
                    screen.blit(dialogue, (-102, 410))
                    screen.blit(text2, (40, 486))
                    pygame.display.flip()




            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()