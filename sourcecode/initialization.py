
#simple pygame initialisation will fill screen white

import pygame

pygame.init()                                   
screen = pygame.display.set_mode((1280, 720))       #Screen size
clock = pygame.time.Clock()                         #time
running = True                                      #this should be obvious

while running:
    for event in pygame.event.get():
        pressed= pygame.key.get_pressed()
        if pressed[pygame.K_ESCAPE]:                #if escape key pressed quit
            running = False
        if event.type == pygame.QUIT:
            running = False
        screen.fill("black")
        pygame.display.flip()                       #updates entire screen
