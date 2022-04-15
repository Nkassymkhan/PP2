from platform import platform
import pygame as pg
import sys
import random
import time

# initializing
pg.init()

#Global values
FPS = 60
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
STEP = 3
ENEMY_STEP = 6
SCORE = 0
COIN = 0

# colors 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

clock = pg.time.Clock()
#Font
score_font = pg.font.SysFont("Verdana", 20)
gameover_font = pg.font.SysFont("ComicSans", 50)
gameover = gameover_font.render("Game Over", True, BLACK)
score_coin_font = pg.font.SysFont("Verdana", 20)

#Screen
SURF = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pg.display.set_caption("Street Racer")
#Background
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
        self.image = pg.image.load("images/Coin.png")
        self.image = pg.transform.scale(self.image,(40, 40))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), random.randint(40, SCREEN_HEIGHT - 40))
    def draw(self, surface):
        surface.blit(self.image, self.rect)
    def update(self):
        self.rect.move_ip(0, 0)
        
#Sprites and Sprite groups
P1 = Player()
E1 = Enemy()
C1 = Coin()

enemies = pg.sprite.Group()
enemies.add(E1)
coins = pg.sprite.Group()
coins.add(C1)


all_sprites = pg.sprite.Group()
all_sprites.add(E1)
all_sprites.add(P1)
all_sprites.add(C1)


#main cycle
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    P1.update()
    E1.update()
    C1.update()

    #blit on surface all sprites
    for entity in all_sprites:
            SURF.blit(entity.image, entity.rect)
            entity.update()    
    
    #collide between Player and Enemy
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
    #Collide between Player and Coins
    if pg.sprite.spritecollideany(P1, coins):
        COIN += 1
        if C1 in pg.sprite.spritecollide(P1, coins, True):
            C1 = Coin()
            coins.add(C1)   
    
    #Blit background on surface
    SURF.blit(bg, (0, 0))

    E1.draw(SURF)
    P1.draw(SURF)
    C1.draw(SURF)
    #Score and amount of coins
    score_img = score_font.render(f"SCORE:{SCORE}", True, BLACK)
    score_coin_img = score_coin_font.render(f"COINS:{COIN}", True, BLACK)
    SURF.blit(score_img, (10, 10))
    SURF.blit(score_coin_img, (10, 50))
    
    pg.display.update()
    clock.tick(FPS)
    pg.display.flip()