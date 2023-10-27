
#simple pygame initialisation will fill screen white

import pygame
  
def make_settings(screen):
    pygame.init()   
                                           #Screen size
    clock = pygame.time.Clock()                         #time
    running = True
    GREEN = pygame.Color(0,255,0) 
    BLACK = pygame.Color(0,0,0)    
    THEME1= [GREEN, BLACK]                                 #this should be obvious
    def make_frame(colorTheme):
        frameCenter = [1280/2,720/2]
        frameSize = [1210,700]
        frameXYDimes = [frameCenter[0]-frameSize[0]/2,frameCenter[1]-frameSize[1]/2]  
        frameborder = 5
        frame = pygame.Rect(frameXYDimes[0],frameXYDimes[1], frameSize[0], frameSize[1])
        frameContent = pygame.Rect(frameXYDimes[0] + frameborder,frameXYDimes[1] + frameborder, frameSize[0] - 2 * frameborder, frameSize[1] - 2 * frameborder)
        pygame.draw.rect(screen,colorTheme[0],frame)
        pygame.draw.rect(screen,colorTheme[1],frameContent)

    while running:   
        for event in pygame.event.get():             
            if event.type == pygame.QUIT:
                running = False
        make_frame(THEME1)
        pygame.display.flip()