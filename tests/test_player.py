
import unittest
import pygame, os



# ovaj test, proverava, da li se class Player ship dobro draw-uje na ekran...
# python -m unittest test_player.py

PLAYER_SPACESHIP = pygame.image.load(os.path.join("..","images", "player.png"))

class Ship:
    """
        Ship Parent class to inherit player and enemy ship class

    """

    # pozicija ship-a
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ship_img = None
    
    # draw ship na ekranu
    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))

    # funkcija da se dobije širina ship-a, image-a
    def get_width(self):
        return self.ship_img.get_width()
    
    # funkcija da se dobije visina ship-a, image-a
    def get_height(self):
        return self.ship_img.get_height()


class Player(Ship):
    """
    Player Ship class which inherits from Ship class


    1. The line of code self.mask = pygame.mask.from_surface(self.ship_img) creates a collision mask for the enemy ship based on its image.
    A collision mask is a Mask object that is used to detect collisions between two objects in a game. The from_surface method of the pygame.mask module creates a Mask object from a given image Surface.

    """

    # pozicija ship-a
    def __init__(self, x, y):
        super().__init__(x, y)

        # 1. u docs
        self.ship_img = PLAYER_SPACESHIP  # postavljanje slike za ovaj ship
        self.mask = pygame.mask.from_surface(self.ship_img)  
    
    
    # draw ship na ekranu, koristi funkciju od superclass (parent class..)
    def draw(self, window):
        super().draw(window)





class TestShip(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pygame.init()
        cls.window = pygame.display.set_mode((800, 800))

    @classmethod
    def tearDownClass(cls):
        pygame.quit()
    
    def test_init(self):
        ship = Player(100, 200)
        self.assertEqual(ship.x, 100)
        self.assertEqual(ship.y, 200)
        self.assertIsNotNone(ship.ship_img)

    def test_draw(self):
        ship = Player(100, 200)
        # set the ship image for testing purposes
        ship.ship_img = pygame.Surface((50, 50))
        ship.ship_img.fill((255, 255, 255))
        # call the draw method
        ship.draw(self.window)
        # check if the ship was drawn correctly
        pixels = pygame.PixelArray(self.window)
        self.assertEqual(pixels[100][200], 16777215)
        pixels.close()

    def test_get_width(self):
        ship = Player(100, 200)
        # set the ship image for testing purposes
        ship.ship_img = pygame.Surface((50, 50))
        width = ship.get_width()
        self.assertEqual(width, 50)

    def test_get_height(self):
        ship = Player(100, 200)
        # set the ship image for testing purposes
        ship.ship_img = pygame.Surface((50, 70))
        height = ship.get_height()
        self.assertEqual(height, 70)

if __name__ == '__main__':
    unittest.main()
