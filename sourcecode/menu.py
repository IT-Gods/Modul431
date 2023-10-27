
import pygame
import utils.colors as c
import  os
import utils.helpers as h
import settings as settings
import game_objectified as g
import utils.themes as t





def menu_screen(screen):
    pygame.init()                                   
    #screen = pygame.display.set_mode((1280, 720))       #Screen size
    clock = pygame.time.Clock()                         #time
    running = True  
    DISPLAY_SIZE = [1280,720]  
    
    colorpalette = c.colors() 
    colorTheme= [colorpalette.green(),colorpalette.red(),colorpalette.black(),colorpalette.white()]                                 #this should be obvious
    
   
    THEME_CURR = t.THEME1
    borderMargin = [20, 20]
    
    image=pygame.image.load(os.path.join("DesignElements/enemy-element2.jpeg"))   
    welcome = pygame.transform.scale(image, [DISPLAY_SIZE[0] / 5 ,DISPLAY_SIZE[1] / 5 ] )
    image_rect = welcome.get_rect()
    image_rect.centerx = DISPLAY_SIZE[0] // 2  
    image_rect.top = 50

    
    
  
    
    #variables
    select = 0
    timesSelect = 0


    #size parameters

    screenMiddle = [1280/2,720/2]


    borderMargin = [20, 20]
    playgroundSafeArea = [[borderMargin[0], borderMargin[1]],[DISPLAY_SIZE[0]-borderMargin[0], DISPLAY_SIZE[1]-borderMargin[1]]]
    playAreaWidth = [playgroundSafeArea[1][0]-playgroundSafeArea[0][0], playgroundSafeArea[1][1]-playgroundSafeArea[0][1]]
    playAreaRect = pygame.Rect(playgroundSafeArea[0][0], playgroundSafeArea[0][1], playAreaWidth[0], playAreaWidth[1])
    # menuWallSize = [1210,700]
    # menuWallXY = [screenMiddle[0]-menuWallSize[0]/2,screenMiddle[1]-menuWallSize[1]/2]  
    # borderWall = 5

    selectOptionSize = [150,75]
    selectOptionSpace = 100
    selectOptionXY = [screenMiddle[0] - 150 , screenMiddle[1] ]

    #color parameters




    # menuWall1 = pygame.Rect(menuWallXY[0],menuWallXY[1],menuWallSize[0],menuWallSize[1])
    # menuWall2 = pygame.Rect(menuWallXY[0] + borderWall , menuWallXY[1] + borderWall , menuWallSize[0] - 2 * borderWall , menuWallSize[1] - 2 * borderWall)

    
    selectOptionXY[1]+timesSelect*selectOptionSpace,selectOptionSize[0],selectOptionSize[1]

    selectOption1 = pygame.Rect(selectOptionXY[0]+timesSelect*selectOptionSpace , selectOptionXY[1],selectOptionSize[0],selectOptionSize[1])
    timesSelect+=1
    selectOption2 = pygame.Rect(selectOptionXY[0] +timesSelect*selectOptionSpace * 2, selectOptionXY[1],selectOptionSize[0],selectOptionSize[1])
    timesSelect += 1
    selectOption3 = pygame.Rect(selectOptionXY[0] +timesSelect*selectOptionSpace / 2 , screenMiddle[1] + 150,selectOptionSize[0],selectOptionSize[1])
    timesSelect += 1
    font = pygame.font.Font('freesansbold.ttf', 20)

   
    
    
    
    while running:
        pressed = pygame.key.get_pressed()    
        for event in pygame.event.get():             
            if event.type == pygame.QUIT:
                running = False
            if pressed[pygame.K_UP]:
                outcome = settings.make_settings(screen)
                match outcome:
                    case 1:
                        THEME_CURR = t.THEME1
                    case 2:
                        THEME_CURR = t.THEME2
                    case 3:
                        THEME_CURR = t.THEME3
            if pressed[pygame.K_LEFT]:
                game_running = True
                while game_running:
                    outcome = g.run_game(1,1,THEME_CURR)
                    if outcome == 1:
                        lvl += 1
                    if outcome == -1:
                        game_running = False
                    if outcome == -2:
                        running = False
                        game_running = False
            if pressed[pygame.K_RIGHT]:
                game_running = True
                while game_running:
                    outcome =   g.run_game(1,2,THEME_CURR)
                    if outcome == 1:
                        lvl += 1
                    if outcome == -1:
                        game_running = False
                    if outcome == -2:
                        running = False
                        game_running = False

        screen.fill("green")
        pygame.draw.rect(screen,colorTheme[2],playAreaRect)
        # pygame.draw.rect(screen,colorTheme[2],menuWall2)
        screen.blit(welcome, image_rect)
        pygame.draw.rect(screen,colorTheme[0],selectOption1)
        screen.blit(font.render('Single', True, colorTheme[3]), (selectOption1.centerx - 25 , selectOption1.centery - 10))
        pygame.draw.rect(screen,colorTheme[0],selectOption2)
        
        screen.blit(font.render('Multi', True, colorTheme[3]), (selectOption2.centerx - 25, selectOption2.centery - 10))
        pygame.draw.rect(screen,colorTheme[0],selectOption3)
    
        screen.blit(font.render('Settings', True, colorTheme[3]), (selectOption3.centerx - 39, selectOption3.centery - 10) )

    
    
    
    
            
                    

    
 

            

              
    
        pygame.display.flip()
    
    
    
    




