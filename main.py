import pygame, sys, os
from pygame.locals import *
import random
import math



#background music
from pygame import mixer

# random words
from words import get_rand_word


# pygame init
pygame.init()



#set up window
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("X-Galactic-Blitz")


# background
BG = pygame.transform.scale(pygame.image.load(os.path.join("images", "background-black.png")), (WIDTH, HEIGHT)).convert()

BG_launch = pygame.transform.scale(pygame.image.load(os.path.join("images", "elon_space.png")), (WIDTH, HEIGHT)).convert()

# LOAD SPACESHIPS

PLAYER_SPACESHIP = pygame.image.load(os.path.join("images", "player.png"))

ENEMY1= pygame.image.load(os.path.join("images", "enemy1.png"))
ENEMY2 = pygame.image.load(os.path.join("images", "enemy2.png"))
ENEMY3 = pygame.image.load(os.path.join("images", "enemy3.png"))
ENEMY4= pygame.image.load(os.path.join("images", "enemy4.png"))
ENEMY5 = pygame.image.load(os.path.join("images", "enemy5.png"))
ENEMY6 = pygame.image.load(os.path.join("images", "enemy6.png"))
ENEMY7 = pygame.image.load(os.path.join("images", "enemy7.png"))





 
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


        WIN.blit(label, (x + self.ship_img.get_width() // 2 - label.get_width() // 2, y + self.ship_img.get_height() + 5))
        WIN.blit(self.ship_img, (x, y))


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


def collide(obj1, obj2):
    """

    Funkcija za detekciju collisions

    - Posto su enemy i player objekti, mi prosleđujemo: `collide(enemy, player)`, 
    sto znaci, da je prvi objekat enemy ship, drugi objekat player ship 

    """

    offset_x = obj2.x - obj1.x   
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None


def background_music():
    """
        load and start background music


    """

    # background music
    mixer.init()                     # Starting the mixer
    mixer.music.load(os.path.join("music", "Elon-Musk-dont-doubt-your-vibe.ogg"))     # Loading the song 
    mixer.music.set_volume(0.7)      # Setting the volume
    mixer.music.play()               # Start playing the song


def stop_music():
    """
        stop background music

    """

    mixer.music.stop()



# --------------------


# Map the key codes to characters
keymap = {
    pygame.K_a: 'a',
    pygame.K_b: 'b',
    pygame.K_c: 'c',
    pygame.K_d: 'd',
    pygame.K_e: 'e',
    pygame.K_f: 'f',
    pygame.K_g: 'g',
    pygame.K_h: 'h',
    pygame.K_i: 'i',
    pygame.K_j: 'j',
    pygame.K_k: 'k',
    pygame.K_l: 'l',
    pygame.K_m: 'm',
    pygame.K_n: 'n',
    pygame.K_o: 'o',
    pygame.K_p: 'p',
    pygame.K_q: 'q',
    pygame.K_r: 'r',
    pygame.K_s: 's',
    pygame.K_t: 't',
    pygame.K_u: 'u',
    pygame.K_v: 'v',
    pygame.K_w: 'w',
    pygame.K_x: 'x',
    pygame.K_y: 'y',
    pygame.K_z: 'z'
}

# --------------------


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


                #ustvari, proveri, da li neki objekat, ima assigned, koji je rezervisan, ako nije, onda tek rezervise koji odgovara ! 
                # ovo je van objekta ! 
                # ako je ovo true, onda to znaci, da je rezervisan objekat, i da, mozemo se upustiti da proverimo, koji je to objekat
                if rezervisan_objekat:
                    #ako je ovo taj koji je izabran i na kome radis, onda , njega, ces da brises karakter.. 
                    # on ce izlistati kroz ove elemente, i koji objekat bude imao aktivan boolean, to je objekat koji treba da obrises mu karakter , ne brini za ovaj drugi else, zato sto je on ovde izvrsio, znamo da je on assigned
                    # i da ovaj drugi uslov, je da slovo mora biti slovo koje trazimo, inace bilo koje slovo ce prihvatiti, a ne moze.. nego samo to koje se trazi..
                    if enemy.aktivan() and slovo == enemy.get_first_char():
                            enemy.delete_first_character()

                            # i ovde moze da proveri da li je to zadnji, da bi resetovao.. kao i unistio objekat
                            # moze se obrisati, lista direktno odavde, jer referencom ide sve to..
                            # ovo je da proveri, treba biti 1, i onda radi ovaj funkcija.. 
                            if enemy.is_name_empty():
                                # nema vise ovog objekta, release lock
                                rezervisan_objekat = 0
                                
                                # i sada ga sklanja sa liste ! 
                                enemies.remove(enemy)




                else:
                    # onda pronadji objekat koji odgovara ka ovome (ne brini, prvi koji naidje, lock-ovace ga.. cak i ako je van ekrana, to moze neko da resi.. kasnije)
                    if slovo == enemy.get_first_char():
                            enemy.delete_first_character()

                            # i ovde moze da proveri da li je to zadnji, da bi resetovao.. kao i unistio objekat
                            # moze se obrisati, lista direktno odavde, jer referencom ide sve to..
                            # ovo je da proveri, treba biti 1, i onda radi ovaj funkcija.. 
                            if enemy.is_name_empty():
                                # nema vise ovog objekta
                                rezervisan_objekat = 0
                                # i sada ga sklanja sa liste ! 

                                # i sada ga sklanja sa liste ! 
                                enemies.remove(enemy)

                            else:
                                # da podesi aktivan varijablu na true, u tom objektu
                                enemy.reserve()

                                # e evo ga, kada nadjemo neki.. onda ga lockuje.. 
                                rezervisan_objekat = 1



# --------------------



def main():
    """
        glavni dio funkcionalnosti, koji pokreće aplikaciju i sve njene funkcije (main loop... )




    """


    # background music 
    background_music()

    # game states
    run = True
    lost = False
    lost_count = 0
    level = 0
    lives = 3

    # perfomanse
    FPS = 60

    # brzina enemy-a
    ENEMY_VEL = 3
    
    # enemy list, koji se povecava sa level-ima
    enemies = []

    # ovo je, koliko enemies, ce biti učitano u sledeći level ! svaki sledeci level, ce ovo da se poveca za +5. time, izazivajući, da imamo +5 enemies u odnosu naprethodni put.. 
    wave_length = 0


    # font 
    main_font = pygame.font.SysFont("comicsans", size= 50)

    # postavljanje player ship u centru (ali necemo ga morati pomerati, zato u main event loop, nemamo, nikakve event listeners za player, jer nam ne trebaju u ovoj igri. cilj, je samo iskucati enemies, da se uniste na taj nacin )
    player = Player(340, 480)

    # za redrawing.. 
    clock = pygame.time.Clock()


    # scrollable backgound --------------

    # za scroll, varijabla
    scroll = 0

    tiles = math.ceil(HEIGHT / BG.get_height()) + 1

    # --------------

    scrolling = 1 # dokle god je ovo aktivno, radice scroll, kada je neaktivno, onda scroll stane, to na end game



    def redraw_window(WIN, BG, scroll, tiles):

        # DRAWING THE BACKGROUND (static)
        #WIN.blit(BG, (0,0))

        # scrollable backgound --------------
        i = 0
        while i < tiles:
            WIN.blit(BG, (0, scroll + BG.get_height() * i))
            i += 1




        scroll += 35

        if scroll > 0:
            scroll = -BG.get_height() * (tiles - 1)
        
        # --------------

        # DRAW TEXT
        level_label = main_font.render(f"Level: {level}", 1, (255,255,255))  #level
        lives_label = main_font.render(f"Lives: {lives}", 1, (255,255,255))  #lives 
        WIN.blit(lives_label, (10, 10)) # lives se stavlja na ekran, na poziciji, gornji levi ugao
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10)) # level se stavlja na ekran, na poziciji, gornji desni ugao


        # SHIP DRAWING (drawuj, sve enemies koje imas u listi... zato koristimo for loop..)
        for enemy in enemies:
            enemy.draw(WIN)

        # takodje, drawuj, i player (posto se ne pomera, ovo ni ne mora, ali neka stoji u jednoj funkciji)
        player.draw(WIN)
        

        # IF WE LOSE
        if lost:
            lost_label = main_font.render("YOU LOST!", 1, (255,255,255)) # da kreira label
            WIN.blit(lost_label, ((WIDTH-lost_label.get_width())//2, (HEIGHT-lost_label.get_height())//2)) # i da ga prikaze na ekranu



        # UPDATING THE DISPLAY
        pygame.display.update()

        # ovo return-uje scroll varijablu za scrollable background
        return scroll
    


    # main game loop
    while True: 
        

        


        #na osnovu clock, jer clock, ce praviti pauze, da ne bi zbog infinite while loop, PC uzimao resurse previse, tj. da ne bi redraw previse često
        clock.tick(FPS)

        #just like, just stop, sledeci ko bude pravio game over interaktivnije, treba da zaustavi scrolling, na bolji nacin ? il tako nesto
        if scrolling == 1:
            scroll = redraw_window(WIN, BG, scroll, tiles) # UPDATING DISPLAY |  ovo return-uje scroll varijablu za scrollable background
        else:
            #ovo samo da handluje, lost text
            # IF WE LOSE
            if lost:
                try_again_label = main_font.render("To try again, press any key", 1, (255, 255, 255)) # creates the "Try again" label
                lost_label = main_font.render("YOU LOST!", 1, (255,255,255)) # da kreira label
                WIN.blit(lost_label, ((WIDTH-lost_label.get_width())//2, (HEIGHT-lost_label.get_height())//2)) # i da ga prikaze na ekranu
                WIN.blit(try_again_label, ((WIDTH-try_again_label.get_width())//2, (HEIGHT-lost_label.get_height())//2 + 50))

                # UPDATING THE DISPLAY
                pygame.display.update()


                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    # obrisi prvo slovo, sa bilo koji key, samo pocetak, da li radi
                    elif event.type == pygame.KEYDOWN:
                        main()











        
        """

        # provera, da li imamo dovoljno zivota, da nastavimo igrati. 

        - Check if the number of remaining lives is less than or equal to 0. If it is, set the lost variable to True, which indicates that the game has been lost. Also, increment the lost_count variable by 1.


        - Ako je igra izgubljena jer nema vise zivota, onda u sledeci if case (odmah posle ovog, ne ceka sledeci loop), on ce da proveri da li je 'lost' varijable True. ako jeste, onda, ce da proveri, da li je igra izgubljena duze od 3 sekundi (znaci, 'lost_count' ce da se povecava, dok ne dodje do 3 sekundi.. ). i onda 'run' varijabla ce se stavit na False. sto ce 'halt-ovati' main loop (zato sto u sami while loop stoji: 'while run: ' , sto znaci, da while petlja izvrsava, dokle god, je run True.. sto u ovaj slucaj, pri sledecoj iteraciji za while petlju, nece biti True, i igra ce se zaustaviti

        

        )

        - I takodje, ako smo izgubili, varijabla 'lost' ce biti na True, i time ce se zaustaviti sve sto se kretalo, i nece moci da se krece nista vise. 
        I ovaj 
        # IF WE LOSE
        if lost:
            lost_label = main_font.render("YOU LOST!", 1, (255,255,255)) # da kreira label
            WIN.blit(lost_label, ((WIDTH-lost_label.get_width())//2, (HEIGHT-lost_label.get_height())//2)) # i da ga prikaze na ekranu

        dio, ce da se execute i prikaze, kada se igra izgubi !  i time zavrsavajuci igru.. to je to..



        """
        # provera, da li imamo dovoljno zivota, da nastavimo igrati. 
        if lives <= 0:
            lost = True  
            stop_music()
            scrolling = 0
            lost_count += 1
        if lost:
            if lost_count > FPS*3:
                run = False
            else:
                continue
            

        # ADDING ENEMIES IN THE LIST AND SPAWNING THEM 
        # kada se svi enemies uniste, onda je lista prazna, i onda, dodamo nove varijable..
        if len(enemies) == 0:
            level += 1   
            wave_length += 5  # +5 enemyes
            ENEMY_VEL += 0.1  #takodje, da se poveca brzina


            # i sada, ce ova funkcija, da kreira, toliko novih, objekata Enemy-a. u zavisnosti od wave_lenght, koji je, koliko enemy-a ce biti sada u ovaj level..
            for _ in range(wave_length):

                # uzmi novu random word
                word = get_rand_word()

                # podseti se, konstruktor za Enemy je: def __init__(self, x, y, color):, tako da su ovo samo parametri, da 'x' i 'y' pozicija bude random 

                enemy = Enemy(random.randrange(50, WIDTH-100), random.randrange(-1500 *(1+level//4), -100), random.choice(["enemy1", "enemy2", "enemy3", "enemy4", "enemy5", "enemy6", "enemy7"]), word)
                # i to se doda u postojecoj listi... 
                enemies.append(enemy)


        # vazi za svaki enemy objekat, u listi
        for enemy in enemies[:]:
            enemy.move(ENEMY_VEL) #pokrece enemy-a, ka dole.. 

            # ako se sudare enemy, i player, gubis live
            # takodje, i ako enemy, predje ispod ekrana.. nisi ga unistio pre nego je uspeo da pobegne
            # collide funkcija, ce vratiti True, ako su se collide-ovali ! a False ako ne (i time se ovo nece izvrsiti). vidi objasnjenje za collide funkciju kako radi, kod 'return' je to.. 
            if collide(enemy, player):
                lives -= 1
                enemies.remove(enemy)
            elif enemy.y + enemy.get_height() > HEIGHT:
                lives -= 1
                enemies.remove(enemy)




        # checking for events ********** 
        for event in pygame.event.get():

            # quit if X button pressed (in window)
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                

            # obrisi prvo slovo, sa bilo koji key, samo pocetak, da li radi
            if event.type == pygame.KEYDOWN:

                #                for enemy in enemies:
                #                    #enemy.draw(WIN)
                #                    enemy.delete_first_character()

                # prepoznaje koji key je pressed, engleska abeceda.. 
                if event.key in keymap:
                    #pass koji je karakter ubačen.. 
                     uklanjanje_karaktera_s_labela(keymap[event.key], enemies)


        # checking for events ********** 


        # redraw (update) screen. samo funkcija za redrawing je dovoljna jednom da se zove
        #pygame.display.update()




def main_menu():
    """
        Prva funkcija koja se pokreće, spawnuje main() (main loop programa), restartuje main loop kada se završi igra


    """

    sub_title_font = pygame.font.SysFont("comicsans", 40)
    title_font = pygame.font.SysFont("comicsans", 50)
    run = True

    while run:
        
        # set title
        title_label = title_font.render("X-Galactic-Blitz: Defending Earth with SpaceX", 1, (255,255,255))
        sub_title_label = sub_title_font.render("Press any key to begin...", 1, (255,255,255))
        sub_title_label2 = sub_title_font.render("Enjoy my game - Elon Musk", 1, (255,255,255))


        WIN.blit(BG_launch, (0,0))

        WIN.blit(title_label, ((WIDTH-title_label.get_width())//2, (HEIGHT-title_label.get_height())//2 - 50))
        WIN.blit(sub_title_label, ((WIDTH-sub_title_label.get_width())//2, (HEIGHT-sub_title_label.get_height())//2 + 50))
        WIN.blit(sub_title_label2, ((WIDTH-sub_title_label2.get_width())//2, (HEIGHT-sub_title_label2.get_height())//2 + 130))

        pygame.display.update()

        # čeka na event, ako pritisne bilo koje dugme, da pocne igra..
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            #start, on any key
            if event.type == pygame.KEYDOWN:
                main()

    pygame.quit()



# prvo prikaze, da bi poceo igru.. (kvazi launch screen)
main_menu()
