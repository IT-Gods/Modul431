
import pygame
import utils.colors as c
import  os
import utils.helpers as h
import settings as settings
import menu as menu


def make_settings(screen):
    pygame.init()                                   
    clock = pygame.time.Clock()                 
    running = True  
    DISPLAY_SIZE = [1280,720]  
    
    colorpalette = c.colors() 
    colorTheme= [colorpalette.green(),colorpalette.red(),colorpalette.black(),colorpalette.white()]                                 #this should be obvious
    
    borderMargin = [20, 20]

    themeSize = 20
    font = pygame.font.Font('freesansbold.ttf', themeSize)
    titleSize = 80
    fontTitle = pygame.font.Font('freesansbold.ttf', titleSize)
    
    select = 0
    timesSelect = 0
    screenMiddle = [1280/2,720/2]
    borderMargin = [20, 20]
    playgroundSafeArea = [[borderMargin[0], borderMargin[1]],[DISPLAY_SIZE[0]-borderMargin[0], DISPLAY_SIZE[1]-borderMargin[1]]]
    playAreaWidth = [playgroundSafeArea[1][0]-playgroundSafeArea[0][0], playgroundSafeArea[1][1]-playgroundSafeArea[0][1]]
    playAreaRect = pygame.Rect(playgroundSafeArea[0][0], playgroundSafeArea[0][1], playAreaWidth[0], playAreaWidth[1])
    selectOptionSize = [150,75]
    selectOptionSpace = 100
    selectOptionXY = [screenMiddle[0] - 3 * (selectOptionSize[0] / 2) - selectOptionSpace / 2, screenMiddle[1] ]

    screen.fill("green")
    pygame.draw.rect(screen,colorTheme[2],playAreaRect)



    screen.blit(fontTitle.render('Settings', True, colorTheme[0]), (DISPLAY_SIZE[0] / 2 - 2 * titleSize  , 50))


    selectOptionXY[1]+timesSelect*selectOptionSpace,selectOptionSize[0],selectOptionSize[1]

    selectOption1 = pygame.Rect(selectOptionXY[0]+timesSelect*selectOptionSpace , selectOptionXY[1],selectOptionSize[0],selectOptionSize[1])
    timesSelect+=1
    selectOption2 = pygame.Rect(selectOptionXY[0] +timesSelect*selectOptionSpace * 2, selectOptionXY[1],selectOptionSize[0],selectOptionSize[1])
    timesSelect += 1
    selectOption3 = pygame.Rect(selectOptionXY[0] +timesSelect*selectOptionSpace * 2 , screenMiddle[1] ,selectOptionSize[0],selectOptionSize[1])
    timesSelect += 1
   
    pygame.draw.rect(screen,colorTheme[0],selectOption1)
    screen.blit(font.render('green', True, colorTheme[3]), (selectOption1.centerx -   themeSize - 6  , selectOption1.centery - 10))
    pygame.draw.rect(screen,colorTheme[0],selectOption2)
    
    screen.blit(font.render('Blue', True, colorTheme[3]), (selectOption2.centerx - themeSize , selectOption2.centery - 10))
    pygame.draw.rect(screen,colorTheme[0],selectOption3)

    screen.blit(font.render('Red', True, colorTheme[3]), (selectOption3.centerx -  themeSize , selectOption3.centery - 10) )

    
    while running:
        pressed = pygame.key.get_pressed()    
        for event in pygame.event.get():             
            if event.type == pygame.QUIT:
                running = False
            if pressed[pygame.K_1]:
                return 1 
               
            elif pressed[pygame.K_2]:
                return 2 
                
            elif pressed[pygame.K_3]:
                return 3 
              
            elif pressed[pygame.K_ESCAPE]:
                menu.menu_screen(screen)
            elif pressed[pygame.K_KP_ENTER]:
                running = False
        pygame.display.flip()
    
    
    



