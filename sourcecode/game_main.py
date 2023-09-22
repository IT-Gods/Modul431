
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
playerSize = [20,20]
playerXY = [(DISPLAY_SIZE[0]-playerSize[0])/2,(DISPLAY_SIZE[1]*7/8)-playerSize[1]/2]

bulletSize = [5,15]
bulletXY = [playerXY[0]-playerSize[0]/2, playerXY[1]-playerSize[1]/2]
bulletHere = False

playgroundSafeAreas = [20, 20]


xCoordinateValue = 5
yCoordinateValue = 2 
enemySize = [DISPLAY_SIZE[0] / 30, DISPLAY_SIZE[0] / 30]
enemyDist = [enemySize[0] / 1.2, enemySize[1] / 1.2]
# it detemines the most top left coordinate of the enemies and it accounts for the amount of the enemies their size and the spaces between them to make the enemies start centered on the x coordinate.
enemyXY = [(DISPLAY_SIZE[0] / 2) - (xCoordinateValue * enemySize[0] )- (4.5 * enemyDist[0]),(DISPLAY_SIZE[1] / 3) - (yCoordinateValue * enemySize[1]) - (1.5 * enemyDist[1]) ]
enemyAlive = [[True, True, True, True],[True, True, True, True],[True, True, True, True],[True, True, True, True],[True, True, True, True],
    [True, True, True, True],[True, True, True, True],[True, True, True, True],[True, True, True, True],[True, True, True, True]]
enemyDir = 1
enemyDead = [0,10]

#bullet directions
bulletUp = -1
bulletDown = 1
#general vars
enemiesRow = 0
enemiesColumn = 0

#main game loop
while running:
   

    
    pressed = pygame.key.get_pressed()
  
    g.make_playground(screen,DISPLAY_SIZE,THEME1, playgroundSafeAreas[0],playgroundSafeAreas[1] )
    for event in pygame.event.get():
        if pressed[pygame.K_ESCAPE]:                #if escape key pressed quit
            running = False
        if event.type == pygame.QUIT:
            running = False
        if pressed[pygame.K_SPACE]:                 #if spacebar is pressed make a bullet
            if bulletHere == False:                 #checks if bullet on screen
                bulletXY=[playerXY[0]+playerSize[0]/2-(bulletSize[0]/2),playerXY[1]-playerSize[1]/2]
                bulletXY = g.updateFire(THEME1[1],bulletXY,bulletSize,screen,bulletUp)
                bulletHere = True
    # Implement the enemies
    xyEnemy= g.moveEnemiesX(enemyXY,enemyDir)
    xyEnemy , enemyDir = g.collisionEnemies(enemyXY,g.calculateXTopRight(enemyXY,enemySize,enemyDist),DISPLAY_SIZE,enemyDir,enemySize,enemyDist,enemyDead, playgroundSafeAreas)

    
    g.makeEnemies(THEME1[3],enemyXY, enemySize, screen,enemyAlive ,enemyDist)

  


            
    if bulletHere:  #moves bullet if present and checks collision
        g.updateFire(THEME1[1],bulletXY,bulletSize,screen,bulletUp)
        bulletHere = g.detectCollisionEnemies(bulletXY,bulletSize,enemyXY,enemySize,enemyDist,enemyAlive)
    enemyDead = g.rowDead(enemyDead,enemyAlive)


    if bulletHere:
        bulletHere = g.detectCollisionBorder(bulletXY,bulletSize,DISPLAY_SIZE)

    #create player model and update movement
    playerXY = g.updatePlayerXY(playerXY, playerSize,pressed,DISPLAY_SIZE) 
    g.makeRect(THEME1[0],playerXY,playerSize,screen)
    pygame.display.flip()  
   
                    #updates entire screen
