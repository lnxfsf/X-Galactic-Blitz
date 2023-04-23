import pygame, sys, os
from pygame.locals import *
import math

# scroll background, file... 
from scrollable_background import scroll_bg


# pygame init
pygame.init()

#set up window
WIDTH, HEIGHT = 600, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("X-Galactic-Blitz")



# NOVO---------------------- 

# LOAD SPACESHIPS
BLUE_SPACESHIP = pygame.image.load(os.path.join("images", "enemy.png"))
YELLOW_SPACESHIP = pygame.image.load(os.path.join("images", "player.png"))




# NOVO-------------------- 




# main game loop
while True: 
    


    # scroll background, sa fajla funkciju uzima.. 
    scroll_bg(WIN)



    # checking for events ********** 
    for event in pygame.event.get():





        # quit if X button pressed (in window)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    

    # checking for events ********** 


    # redraw (update) screen
    pygame.display.update()



