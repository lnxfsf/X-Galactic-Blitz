import pygame, sys, os
from pygame.locals import *
import math



WIDTH, HEIGHT = 600, 600

def scroll_bg(WIN):
    clock = pygame.time.Clock()
    BG = pygame.transform.scale(pygame.image.load(os.path.join("images", "background-black.png")), (WIDTH, HEIGHT))
    scroll = 0
    tiles = math.ceil(HEIGHT / BG.get_height()) + 1

    while True:
        clock.tick(50)

        i = 0
        while i < tiles:
            WIN.blit(BG, (0, scroll + BG.get_height() * i))
            i += 1

        scroll -= 35

        if abs(scroll) > BG.get_height():
            scroll = 0


        pygame.display.update()

