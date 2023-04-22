import pygame, sys, os
from pygame.locals import *

#handle text input
import pygame_textinput


# pygame init
pygame.init()

#set up window
WIDTH, HEIGHT = 600, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("X-Galactic-Blitz")





# main game loop
while True: 


    # checking for events 
    for event in pygame.event.get():


        # quit if X button pressed (in window)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # redraw (update) screen
    pygame.display.update()



