
import pygame
import utils.colors as c
import  os
import utils.helpers as h
import settings as settings
import game_objectified as g
import utils.themes as t





def menu_screen(screen):
    clock = pygame.time.Clock()                         #time
    pygame.init()                                   
    clock = pygame.time.Clock()                     
    running = True  
    DISPLAY_SIZE = [1280,720]  
    
    colorpalette = c.colors() 
    colorTheme= [colorpalette.green(),colorpalette.red(),colorpalette.black(),colorpalette.white()]                                 #this should be obvious
    lvl = 1   
    score = 0
    THEME_CURR = t.THEME1
    borderMargin = [20, 20]
    
    image=pygame.image.load(os.path.join("DesignElements/enemy-element2.jpeg"))   
    welcome = pygame.transform.scale(image, [DISPLAY_SIZE[0] / 5 ,DISPLAY_SIZE[1] / 5 ] )
    image_rect = welcome.get_rect()
    image_rect.centerx = DISPLAY_SIZE[0] // 2  
    image_rect.top = 50

    select = 0
    timesSelect = 0
    screenMiddle = [1280/2,720/2]


    borderMargin = [20, 20]
    playgroundSafeArea = [[borderMargin[0], borderMargin[1]],[DISPLAY_SIZE[0]-borderMargin[0], DISPLAY_SIZE[1]-borderMargin[1]]]
    playAreaWidth = [playgroundSafeArea[1][0]-playgroundSafeArea[0][0], playgroundSafeArea[1][1]-playgroundSafeArea[0][1]]
    playAreaRect = pygame.Rect(playgroundSafeArea[0][0], playgroundSafeArea[0][1], playAreaWidth[0], playAreaWidth[1])
   

    selectOptionSize = [150,75]
    selectOptionSpace = 100

    selectOptionXY = [screenMiddle[0] - 150 , screenMiddle[1] ]
    selectOptionXY[1]+timesSelect*selectOptionSpace,selectOptionSize[0],selectOptionSize[1]

    selectOption1 = pygame.Rect(selectOptionXY[0]+timesSelect*selectOptionSpace , selectOptionXY[1],selectOptionSize[0],selectOptionSize[1])
    timesSelect+=1
    selectOption2 = pygame.Rect(selectOptionXY[0] +timesSelect*selectOptionSpace * 2, selectOptionXY[1],selectOptionSize[0],selectOptionSize[1])
    timesSelect += 1
    selectOption3 = pygame.Rect(selectOptionXY[0] +timesSelect*selectOptionSpace / 2 , screenMiddle[1] + 150,selectOptionSize[0],selectOptionSize[1])
    timesSelect += 1
    font = pygame.font.Font('freesansbold.ttf', 20)

   
    
    
    
    while running:
        screen.fill("green")
        pygame.draw.rect(screen,colorTheme[2],playAreaRect)
        # pygame.draw.rect(screen,colorTheme[2],menuWall2)
        screen.blit(welcome, image_rect)
        pygame.draw.rect(screen,colorTheme[0],selectOption1)
        screen.blit(font.render('1 Single', True, colorTheme[3]), (selectOption1.centerx - 25 , selectOption1.centery - 10))
        pygame.draw.rect(screen,colorTheme[0],selectOption2)
        
        screen.blit(font.render('2 Multi', True, colorTheme[3]), (selectOption2.centerx - 25, selectOption2.centery - 10))
        pygame.draw.rect(screen,colorTheme[0],selectOption3)
    
        screen.blit(font.render('3 Settings', True, colorTheme[3]), (selectOption3.centerx - 39, selectOption3.centery - 10) )

    
    
    
    
        pressed = pygame.key.get_pressed()    
        for event in pygame.event.get():             
            if event.type == pygame.QUIT:
                running = False
            if pressed[pygame.K_3]:
                outcome = settings.make_settings(screen)
                match outcome:
                    case 1:
                        THEME_CURR = t.THEME1
                    case 2:
                        THEME_CURR = t.THEME2
                    case 3:
                        THEME_CURR = t.THEME3
            if pressed[pygame.K_1]:
                game_running = True
                while game_running:
                    outcome , score =   g.run_game(lvl,1,score,THEME_CURR,screen)
                    if outcome == 1:
                        lvl += 1
                    if outcome == -1:
                        game_running = False
                    if outcome == -2:
                        running = False
                        game_running = False 
                    file = open('Highscore.txt', 'r')
                    comparesc = int(file.read())
                    file.close()
                    file2 = open('Highscore.txt', 'w')
                    if comparesc <= score:
                        file2.write(str(score))
                    else:
                        file2.write(str(comparesc))
                    file.close()

            if pressed[pygame.K_2]:
                game_running = True
                while game_running:
                    outcome , score =   g.run_game(lvl,2, score ,THEME_CURR,screen)
                    if outcome == 1:
                        lvl += 1
                    if outcome == -1:
                        game_running = False
                    if outcome == -2:
                        running = False
                        game_running = False
                    file = open('Highscore.txt', 'r')
                    comparesc = int(file.read())
                    file.close()
                    file2 = open('Highscore.txt', 'w')
                    if comparesc <= score:
                        file2.write(str(score))
                    else:
                        file2.write(str(comparesc))
                    file.close()

           
                    

    
 

            

              
    
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
    
    
    
    




