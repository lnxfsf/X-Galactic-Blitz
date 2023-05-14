

import unittest
import pygame


# ovaj test, proverava, da li collision radi ispravno..
# python -m unittest test_ship.py


def collide(obj1, obj2):
    """

    Funkcija za detekciju collisions

    - Posto su enemy i player objekti, mi prosleđujemo: `collide(enemy, player)`, 
    sto znaci, da je prvi objekat enemy ship, drugi objekat player ship 

    """

    offset_x = obj2.x - obj1.x   
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None


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

class TestShip(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pygame.init()
        cls.window = pygame.display.set_mode((800, 800))

    @classmethod   
    def tearDownClass(cls):
        pygame.quit()
    
    def test_init(self):
        ship = Ship(100, 200)
        self.assertEqual(ship.x, 100)
        self.assertEqual(ship.y, 200)
        self.assertIsNone(ship.ship_img)

    def test_draw(self):
        ship = Ship(100, 200)
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
        ship = Ship(100, 200)
        # set the ship image for testing purposes
        ship.ship_img = pygame.Surface((50, 50))
        width = ship.get_width()
        self.assertEqual(width, 50)

    def test_get_height(self):
        ship = Ship(100, 200)
        # set the ship image for testing purposes
        ship.ship_img = pygame.Surface((50, 70))
        height = ship.get_height()
        self.assertEqual(height, 70)

class TestCollide(unittest.TestCase):
    def test_collide(self):
        # create two ship instances for testing
        enemy = Ship(100, 200)
        player = Ship(150, 250)

        # set the mask for testing purposes
        enemy.mask = pygame.mask.from_surface(pygame.Surface((50, 50)))
        player.mask = pygame.mask.from_surface(pygame.Surface((50, 50)))

        # test collision when ships overlap
        result1 = collide(enemy, player)
        #self.assertTrue(result1) # vraca True, kada je, collision
        self.assertFalse(result1)


        # test collision when ships don't overlap
        player.x = 300
        result = collide(enemy, player)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
