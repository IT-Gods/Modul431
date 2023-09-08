
#simple pygame initialisation will fill screen white

import pygame
import components.py

DISPLAY_SIZE = [1280,720]

pygame.init()
screen = pygame.display.set_mode((DISPLAY_SIZE[0],DISPLAY_SIZE[1]))       #Screen size
clock = pygame.time.Clock()                         #time
running = True                                      #this should be obvious


GREEN = pygame.Color(0,255,0)
RED = pygame.Color(255,0,0)
BLACK = pygame.Color(0,0,0)
WHITE = pygame.Color(255,255,255)

THEME1= [GREEN,RED,BLACK,WHITE]

playerSize = [75,75]
playerXY = [(DISPLAY_SIZE[0]-playerSize[0])/2,(DISPLAY_SIZE[1]*3/4)-playerSize[1]/2]



while running:
    pressed= pygame.key.get_pressed()
    for event in pygame.event.get():
        if pressed[pygame.K_ESCAPE]:                #if escape key pressed quit
            running = False
        if event.type == pygame.QUIT:
            running = False
    updatePlayerXY(playerXY, playerSize)

    screen.fill("black")
        
    makeRect(THEME1,playerXY,playerSize)
    pygame.display.flip()                       #updates entire screen