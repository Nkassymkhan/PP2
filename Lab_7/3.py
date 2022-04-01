import pygame  
from random import randint  
pygame.init()  
  

WIDTH, HEIGHT = 500, 500  
FPS = 30  

WHITE = (255, 255, 255)  
BLACK = (0, 0, 0)  
YELLOW = (255, 255, 0)  
GREEN = (0, 255, 0)  
BLUE = (0, 0, 255)  
 
screen = pygame.display.set_mode((WIDTH, HEIGHT))  
pygame.display.set_caption("CIRCLE")  
  
clock = pygame.time.Clock()  
finished = False  
  
x, y = WIDTH // 2, HEIGHT // 2  
RAD = 25  
dx, dy = 0, 0  
step = 20  
color = YELLOW  
while not finished:  
  
    clock.tick(FPS)  
    screen.fill(WHITE)  
  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            finished = True  
    
    pressed = pygame.key.get_pressed()  
  
    if pressed[pygame.K_UP] and y - RAD  - 15  >= 0:   
           y -= step  
    if pressed[pygame.K_DOWN] and y + RAD + 15 <= HEIGHT:  
           y += step  
    if pressed[pygame.K_LEFT] and x - RAD - 15 >= 0:  
           x -= step  
    if pressed[pygame.K_RIGHT] and x + RAD + 15 <= WIDTH:  
           x += step  
  
    pygame.draw.circle(screen, color, (x, y), RAD)  
  
    pygame.display.flip()  
pygame.quit()