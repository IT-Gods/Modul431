
#simple pygame initialisation will fill screen white

import pygame
import utils.functions as g
DISPLAY_SIZE = [1280,720]

pygame.init()
screen = pygame.display.set_mode((DISPLAY_SIZE[0],DISPLAY_SIZE[1]))       #Screen size
clock = pygame.time.Clock()                         #time
running = True                                      #this should be obvious

#color definitions

GREEN = pygame.Color(0,255,0)
RED = pygame.Color(255,0,0)
BLACK = pygame.Color(0,0,0)
WHITE = pygame.Color(255,255,255)

THEME1= [GREEN,RED,BLACK,WHITE]

#definitions of ingame objects
playerSize = [75,75]
playerXY = [(DISPLAY_SIZE[0]-playerSize[0])/2,(DISPLAY_SIZE[1]*3/4)-playerSize[1]/2]

bulletSize = [50,50]
bulletXY = [playerXY[0]-playerSize[0]/2, playerXY[1]-playerSize[1]/2]
bulletHere = False


#main game loop
while running:

    screen.fill("black")
    
    pressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        if pressed[pygame.K_ESCAPE]:                #if escape key pressed quit
            running = False
        if event.type == pygame.QUIT:
            running = False
        if pressed[pygame.K_SPACE]:                 #if spacebar is pressed make a bullet
            if bulletHere == False:                 #checks if bullet on screen
                bulletXY=[playerXY[0]+(bulletSize[0]/4),playerXY[1]-playerSize[1]/2]
                bulletXY = g.updateFire(THEME1[1],bulletXY,bulletSize,screen)
                bulletHere = True
    
    if bulletHere:  #moves bullet if present and checks collision
        g.updateFire(THEME1[1],bulletXY,bulletSize,screen)
        bulletHere = g.detectCollision(bulletXY,bulletSize,DISPLAY_SIZE)

    
    #create player model and update movement
    playerXY = g.updatePlayerXY(playerXY, playerSize,pressed,DISPLAY_SIZE) 
    g.makeRect(THEME1[0],playerXY,playerSize,screen)
    pygame.display.flip()                       #updates entire screen
