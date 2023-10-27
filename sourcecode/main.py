import pygame
import utils.coreModule as g

pygame.init()                                   
screen = pygame.display.set_mode((1280, 720))       #Screen size
clock = pygame.time.Clock()                         #time
running = True  
DISPLAY_SIZE = [1280,720]                                    #this should be obvious

GREEN = pygame.Color(0,255,0)
RED = pygame.Color(255,0,0)
BLACK = pygame.Color(0,0,0)
WHITE = pygame.Color(255,255,255)

THEME1= [GREEN,RED,BLACK,WHITE]

def make_menu(colorTheme):

    #variables
    select = 0
    timesSelect = 0


    #size parameters

    screenMiddle = [1280/2,720/2]


    menuWallSize = [1210,700]
    menuWallXY = [screenMiddle[0]-menuWallSize[0]/2,screenMiddle[1]-menuWallSize[1]/2]  
    borderWall = 5

    selectOptionSize = [150,75]
    selectOptionSpace = 85
    selectOptionXY = [screenMiddle[0] - selectOptionSize[0]/2 , screenMiddle[1] - selectOptionSize[1]/2 -100]

    #color parameters




    menuWall1 = pygame.Rect(menuWallXY[0],menuWallXY[1],menuWallSize[0],menuWallSize[1])
    menuWall2 = pygame.Rect(menuWallXY[0] + borderWall , menuWallXY[1] + borderWall , menuWallSize[0] - 2 * borderWall , menuWallSize[1] - 2 * borderWall)

    pygame.draw.rect(screen,colorTheme[0],menuWall1)
    pygame.draw.rect(screen,colorTheme[2],menuWall2)

    selectOption1 = pygame.Rect(selectOptionXY[0] , selectOptionXY[1]+timesSelect*selectOptionSpace,selectOptionSize[0],selectOptionSize[1])
    timesSelect+=1
    selectOption2 = pygame.Rect(selectOptionXY[0] , selectOptionXY[1]+timesSelect*selectOptionSpace,selectOptionSize[0],selectOptionSize[1])
    timesSelect += 1
    selectOption3 = pygame.Rect(selectOptionXY[0] , selectOptionXY[1]+timesSelect*selectOptionSpace,selectOptionSize[0],selectOptionSize[1])
    timesSelect += 1
    selectOption4 = pygame.Rect(selectOptionXY[0] , selectOptionXY[1]+timesSelect*selectOptionSpace,selectOptionSize[0],selectOptionSize[1])

    pygame.draw.rect(screen,colorTheme[0],selectOption1)
    pygame.draw.rect(screen,colorTheme[0],selectOption2)
    pygame.draw.rect(screen,colorTheme[0],selectOption3)
    pygame.draw.rect(screen,colorTheme[0],selectOption4)







while running:   
    for event in pygame.event.get():             
        if event.type == pygame.QUIT:
            running = False
   
    make_menu(THEME1)
    pygame.display.flip()








