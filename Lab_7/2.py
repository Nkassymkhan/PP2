import pygame 
from random import randint 
pygame.init() 
 

WIDTH, HEIGHT = 500, 400 
FPS = 20 
 

WHITE = (255, 255, 255) 
BLACK = (0, 0, 0) 
RED = (255, 0, 0) 
GREEN = (0, 255, 0) 
BLUE = (0, 0, 255) 
 
 
screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
pygame.display.set_caption("MUSIC PLAYER") 
 
clock = pygame.time.Clock() 
finished = False 
 
img = pygame.image.load("background.jpg") 
 
playlist = [] 
playlist.append("Perfect.mp3") 
playlist.append("Beggin.mp3") 
playlist.append("Mario.mp3") 
playlist.append("Lovalo.mp3") 
playlist.append("ORDA.mp3") 
 
 
 
def get_next(): 
 
    global playlist 
    playlist = playlist[1:] + [playlist[0]] 
    pygame.mixer.music.load(playlist[0]) 
    pygame.mixer.music.play() 
     
 
pygame.mixer.music.load(playlist.pop())  

pygame.mixer.music.play()   
 
def get_prev(): 
 
    global playlist 
    playlist = [playlist[-1]] + playlist [:-1] 
    pygame.mixer.music.load(playlist[0]) 
    pygame.mixer.music.play() 
 
 
while not finished: 
 
    clock.tick(FPS) 
 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            finished = True 
        screen.blit(img, (0, 0)) 
        if event.type == pygame.KEYDOWN:    
            if event.type==pygame.KEYDOWN: 
                if event.key==pygame.K_LEFT: 
                    get_next() 
                if event.key==pygame.K_RIGHT: 
                    get_prev() 
                if event.key==pygame.K_SPACE: 
                    pygame.mixer.music.pause() 
                if event.key==pygame.K_DOWN: 
                    pygame.mixer.music.unpause() 
 
    pygame.display.flip() 
pygame.quit()