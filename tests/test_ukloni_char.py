import unittest
import pygame, os
import random


# ovaj test proverava, da li brisanje prvog karaktera radi kako treba. znači, da li on označava taj objekat i brise prvi karakter sa tog objekta 
# python -m unittest test_ukloni.py 

level = 0

WIDTH, HEIGHT = 800, 600

ENEMY1= pygame.image.load(os.path.join(".." ,"images", "enemy1.png"))
ENEMY2 = pygame.image.load(os.path.join("..","images", "enemy2.png"))
ENEMY3 = pygame.image.load(os.path.join("..","images", "enemy3.png"))
ENEMY4= pygame.image.load(os.path.join("..","images", "enemy4.png"))
ENEMY5 = pygame.image.load(os.path.join("..","images", "enemy5.png"))
ENEMY6 = pygame.image.load(os.path.join("..","images", "enemy6.png"))
ENEMY7 = pygame.image.load(os.path.join("..","images", "enemy7.png"))

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



class Enemy(Ship):
    """

    Enemy ship class which inherits from ship class


    1. The line of code self.mask = pygame.mask.from_surface(self.ship_img) creates a collision mask for the enemy ship based on its image.
    A collision mask is a Mask object that is used to detect collisions between two objects in a game. The from_surface method of the pygame.mask module creates a Mask object from a given image Surface.

    """


    # random ikonica enemy ship-a.. ovo je dictionary
    COLOR_MAP = {
        "enemy1": (ENEMY1),
        "enemy2": (ENEMY2),
        "enemy3": (ENEMY3),
        "enemy4": (ENEMY4),
        "enemy5": (ENEMY5),
        "enemy6": (ENEMY6),
        "enemy7": (ENEMY7)

    }
    # pozicija ship-a, takodje, u ovaj child, se kreira dodatni argument (override od parent, ovaj dodatni, konstruktor)
    def __init__(self, x, y, color, word):
        super().__init__(x, y)  # draw position
        
        # da li je objekat izabran, kao aktivan
        self.active = False   
        self.word = word

        # bela boja, samo ce biti false, i time je zuta boja
        self.white = True

        # vidi ovo gore docs
        self.ship_img = self.COLOR_MAP[color]  # postavljanje slike za ovaj ship
        self.mask = pygame.mask.from_surface(self.ship_img)


    def get_word(self):
        return self.word

    def set_active(self):
        self.active = True

    # To move down the enemy ship, ovo je definisano samo u ovaj child class.. 
    def move(self, vel): 
        self.y += vel   # on se pokrece, tako sto se njegova y pozicija povećava. znaci, sto je veci y pozicija, on ustvari ide ka dole. a sto je manja y pozicija ide ka gore.. to je po pygame pravila.. 


    def draw(self, window):
        super().draw(window)



        # promeni boju , tako sto ugasi white, i onda ce koristiti (fall back on) zutu boju
        if self.white:
            color = (255, 255, 255)
        else:
            color = (255,255,0)

        font = pygame.font.Font(None, 24)

        label = font.render(self.word, True, color) 
        label_rect = label.get_rect(centerx=self.ship_img.get_width() // 2, top=self.ship_img.get_height() + 5) 


        x = self.x
        y = self.y


        window.blit(label, (x + self.ship_img.get_width() // 2 - label.get_width() // 2, y + self.ship_img.get_height() + 5))
        window.blit(self.ship_img, (x, y))


    #zato sto, ce on da redraw, screen svaki put, samo treba da sklonis prvi karakter iz liste
    def delete_first_character(self):
            if len(self.word) > 0:
                self.word = self.word[1:]

    def get_first_char(self):
        return self.word[0]

    #da li je string empty
    def is_name_empty(self):
            return len(self.word) == 0


    def aktivan(self):
        return self.active

    def reserve(self):
        self.active = True 

        # i promeni boju , tako sto ugasi white, i onda ce koristiti (fall back on) zutu boju
        self.white = False



# na pocetku, nijedan objekat nije rezervisan. tj. nije aktivan nijedan objekat. i on trazi koji bi mogao da rezervise, kada nadje, koji odgovara.. , kada nadje, koji odgovara.. 
rezervisan_objekat = 0


def uklanjanje_karaktera_s_labela(karakter, enemies):
        """
            funkcija da skloni karakter sa label-a

            input parametara je: keymap[event.key], enemies

                keymap[event.key] - vrednost iz dictionary za taj key - dobija samo value ! 
                enemies - enemies lista, (koju on menja direktno.. jer je po referenci.. )

        """

        slovo = karakter
        global rezervisan_objekat

        print(slovo)
        

        #vidi u sve enemies ! 
        for enemy in enemies:
                if rezervisan_objekat:
                    if enemy.aktivan() and slovo == enemy.get_first_char():
                            enemy.delete_first_character()

                            if enemy.is_name_empty():
                                rezervisan_objekat = 0
                                enemies.remove(enemy)

                else:
                    if slovo == enemy.get_first_char():
                            enemy.delete_first_character()


                            if enemy.is_name_empty():
                                rezervisan_objekat = 0
                                enemies.remove(enemy)

                            else:
                                enemy.reserve()
                                rezervisan_objekat = 1





class TestDeletion(unittest.TestCase):

    def test_uklanjanje_karaktera_s_labela(self):

        words = ['apple', 'banana', 'cherry', 'grape' ]
        enemies = []

        # kreiraj objekte
        for word in words:
            # podseti se, konstruktor za Enemy je: def __init__(self, x, y, color):, tako da su ovo samo parametri, da 'x' i 'y' pozicija bude random 
            enemy = Enemy(random.randrange(50, WIDTH-100), random.randrange(-1500 *(1+level//4), -100), random.choice(["enemy1", "enemy2", "enemy3", "enemy4", "enemy5", "enemy6", "enemy7"]), word)
            # i to se doda u postojecoj listi... 
            enemies.append(enemy)


        # prvi parametar predstavlja slovo 'a', da obrise slovo a, drugi listu enemies
        # ako obrises ovo, biće Failing test
        uklanjanje_karaktera_s_labela("a", enemies)

        assert rezervisan_objekat == 1

        # u taj označen objekat, da li je on obrisao ? taj prvi karakter ?
        for enemy in enemies:
            if enemy.aktivan():
                assert enemy.get_word() == "pple"
                assert enemy.aktivan() == True





if __name__ == '__main__':
    unittest.main()
