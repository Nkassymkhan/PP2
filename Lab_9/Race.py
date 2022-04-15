from platform import platform
import pygame as pg
import sys
import random
import time

# initializing
pg.init()
#Global Variables
FPS = 60
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
STEP = 3
ENEMY_STEP = 1
SCORE = 0
COIN = 0
i = 3
#colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

clock = pg.time.Clock()

#Fonts
score_font = pg.font.SysFont("Verdana", 20)
gameover_font = pg.font.SysFont("ComicSans", 50)
gameover = gameover_font.render("Game Over", True, BLACK)
score_coin_font = pg.font.SysFont("Verdana", 20)

#Screen
SURF = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pg.display.set_caption("Street Racer")

bg = pg.image.load("images/AnimatedStreet.png")
#Player
class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("images/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (200, 500)
    def update(self):
        pressed_keys = pg.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[pg.K_LEFT]:
                self.rect.move_ip(-STEP, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[pg.K_RIGHT]:
                self.rect.move_ip(STEP, 0)
        if self.rect.top > 0:
            if pressed_keys[pg.K_UP]:
                self.rect.move_ip(0, -STEP)
        if self.rect.bottom < SCREEN_HEIGHT:
            if pressed_keys[pg.K_DOWN]:
                self.rect.move_ip(0, STEP)
    def draw(self, surface):
        surface.blit(self.image, self.rect)

#Enemy
class Enemy(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("images/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH - 40), 0)
    def update(self):
        global SCORE
        self.rect.move_ip(0, ENEMY_STEP)
        if(self.rect.bottom > SCREEN_HEIGHT):
            SCORE += 1
            self.top = 0
            self.rect.center = (random.randint(30, 350), 0)
    def draw(self, surface):
        surface.blit(self.image, self.rect)
#Coin
class Coin(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pg.Surface((10, 10))
        self.rect = self.surf.get_rect(center = (random.randint(40, SCREEN_WIDTH - 40), random.randint(40, SCREEN_HEIGHT - 40)))

#Sprite
P1 = Player()
E1 = Enemy()
C1 = Coin()
C2 = Coin()
C3 = Coin()


#Sprite groups
enemies = pg.sprite.Group()
enemies.add(E1)
coins = pg.sprite.Group()
coins.add(C1)
coins.add(C2)
coins.add(C3)


all_sprites = pg.sprite.Group()
all_sprites.add(E1)
all_sprites.add(P1)
 

#main cycle
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        

    P1.update()
    E1.update()
    C1.update()
    C2.update()
    C3.update()

    for entity in all_sprites:
            SURF.blit(entity.image, entity.rect)
            entity.update()    
    #Rising of speed of enemy
    if COIN % i == 0 and COIN > 1:
        ENEMY_STEP += 3
        i += 5
        pg.display.update()
    #collide player and enemy
    if pg.sprite.spritecollideany(P1, enemies):
        time.sleep(0.5)
        SURF.fill(WHITE)
        SURF.blit(gameover, (80, 250))
        pg.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(1)
        pg.quit()
        sys.exit()  
    #collide player and coin
    if pg.sprite.spritecollideany(P1, coins):
            if pg.sprite.collide_rect(P1, C1):
                    COIN += 1
                    C1.kill()
                    C1 = Coin()
                    coins.add(C1)

            elif pg.sprite.collide_rect(P1, C2):
                    COIN += 2
                    C2.kill()
                    C2 = Coin()
                    coins.add(C2)
            elif pg.sprite.collide_rect(P1, C3):
                    COIN += 3
                    C3.kill()
                    C3 = Coin()
                    coins.add(C3)
    
   
    SURF.blit(bg, (0, 0))

    E1.draw(SURF)
    P1.draw(SURF)
    #Images of coins
    C1.image = pg.image.load("images\Coin_1.png")
    C2.image = pg.image.load("images\Coin_2.png")
    C3.image = pg.image.load("images\Coin_3.png")

    #Drawing of three coins
    SURF.blit(C3.image, C3.rect)

    SURF.blit(C2.image, C2.rect)
    SURF.blit(C1.image, C1.rect)
    #Score and amount of coins
    score_img = score_font.render(f"SCORE:{SCORE}", True, BLACK)
    score_coin_img = score_coin_font.render(f"COINS:{COIN}", True, BLACK)
    SURF.blit(score_img, (10, 10))
    SURF.blit(score_coin_img, (300, 10))
    
    pg.display.update()
    clock.tick(FPS)