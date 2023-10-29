
#simple pygame initialisation will fill screen white

import os
import pygame
import sys
import menu as menu

import utils.colors as c
import utils.helpers as h


DISPLAY_SIZE = [1280,720]

colorpalette = c.colors()
pygame.init()
 #Screen size
screen = pygame.display.set_mode((DISPLAY_SIZE[0],DISPLAY_SIZE[1]))      
 #time
clock = pygame.time.Clock()                        
running = True  



#color definitions

THEME1= [colorpalette.green(),colorpalette.red(),colorpalette.black(),colorpalette.white()]





borderMargin = [20, 20]

playgroundSafeArea = [[borderMargin[0], borderMargin[1]],[DISPLAY_SIZE[0]-borderMargin[0], DISPLAY_SIZE[1]-borderMargin[1]]]
playAreaWidth = [playgroundSafeArea[1][0]-playgroundSafeArea[0][0], playgroundSafeArea[1][1]-playgroundSafeArea[0][1]]
playAreaRect = pygame.Rect(playgroundSafeArea[0][0], playgroundSafeArea[0][1], playAreaWidth[0], playAreaWidth[1])

welcome = h.adjustImage("DesignElements/space-invaders-org.jpg",DISPLAY_SIZE,screen,[borderMargin[0] + 10,borderMargin[1] + 10], [2,2,2,2])












#main game loop
while running:
    pressed = pygame.key.get_pressed() 
    for event in pygame.event.get():             
        if event.type == pygame.QUIT:
            running = False

        if pressed[pygame.K_SPACE]:  
            menu.menu_screen(screen)
            running = False
            


    screen.fill("green")
    
    pygame.draw.rect(screen, THEME1[2] , playAreaRect)
    screen.blit(welcome[0], (welcome[1],welcome[2])) 


  
   
   


    pygame.display.flip()  

