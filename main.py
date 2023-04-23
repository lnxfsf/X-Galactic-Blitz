import pygame, sys, os
from pygame.locals import *
import math
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




#def scroll_bg(WIN):
#    clock = pygame.time.Clock()
#    BG = pygame.transform.scale(pygame.image.load(os.path.join("images", "background-black.png")), (WIDTH, HEIGHT))
#    scroll = 0
#    tiles = math.ceil(HEIGHT / BG.get_height()) + 1
#
#    while True:
#        clock.tick(50)
#
#        i = 0
#        while i < tiles:
#            WIN.blit(BG, (0, scroll + BG.get_height() * i))
#            i += 1
#
#        scroll -= 35
#
#        if abs(scroll) > BG.get_height():
#            scroll = 0
#
#        for event in pygame.event.get():
#            if event.type == pygame.QUIT:
#                pygame.quit()
#                sys.exit()
#
#        pygame.display.update()
#

# NOVO-------------------- 




# main game loop
while True: 
    


    # scroll background
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



