
#simple pygame initialisation will fill screen white

import pygame

#pimport coreModule as g
DISPLAY_SIZE = [1280,720]

pygame.init()
screen = pygame.display.set_mode((DISPLAY_SIZE[0],DISPLAY_SIZE[1]))       #Screen size
clock = pygame.time.Clock()                         #time
running = True                                      #this should be obvious

#color definitions
#needs to be adjusted to actual themes?
GREEN = pygame.Color(0,255,0)
RED = pygame.Color(255,0,0)
BLACK = pygame.Color(0,0,0)
WHITE = pygame.Color(255,255,255)
PINK = pygame.Color(245, 101, 139)

THEME1= [GREEN,RED,BLACK,WHITE]
THEME2= [PINK, RED, BLACK, WHITE]

#definitions of ingame objects
playerSize = [20,20]
playerXY = [(DISPLAY_SIZE[0]-playerSize[0])/2,(DISPLAY_SIZE[1]*7/8)-playerSize[1]/2]

bulletSize = [5,15]
bulletXY = [playerXY[0]-playerSize[0]/2, playerXY[1]-playerSize[1]/2]
bulletHere = False

borderMargin = [20, 20]

playgroundSafeArea = [[borderMargin[0], borderMargin[1]],[DISPLAY_SIZE[0]-borderMargin[0], DISPLAY_SIZE[1]-borderMargin[1]]]

playAreaWidth = [playgroundSafeArea[1][0]-playgroundSafeArea[0][0], playgroundSafeArea[1][1]-playgroundSafeArea[0][1]]

playAreaRect = pygame.Rect(playgroundSafeArea[0][0], playgroundSafeArea[0][1], playAreaWidth[0], playAreaWidth[1])

xCoordinateValue = 5
yCoordinateValue = 2 
enemySize = [DISPLAY_SIZE[0] / 30, DISPLAY_SIZE[0] / 30]
enemyDist = [enemySize[0] / 1.2, enemySize[1] / 1.2]
# it detemines the most top left coordinate of the enemies and it accounts for the amount of the enemies their size and the spaces between them to make the enemies start centered on the x coordinate.
enemyXY = [(DISPLAY_SIZE[0] / 2) - (xCoordinateValue * enemySize[0] )- (4.5 * enemyDist[0]),(DISPLAY_SIZE[1] / 3) - (yCoordinateValue * enemySize[1]) - (1.5 * enemyDist[1]) ]
enemyAlive = [[True, True, True, True],[True, True, True, True],[True, True, True, True],[True, True, True, True],[True, True, True, True],
    [True, True, True, True],[True, True, True, True],[True, True, True, True],[True, True, True, True],[True, True, True, True]]
enemyLowest = [4,4,4,4,4,4,4,4,4,4]
enemyDir = 1
enemyDead = [0,10]
counter = 0
bullet1Here = False
bullet2Here = False
bullet3Here = False

#bullet directions
bulletUp = -1
bulletDown = 1
#general vars
enemiesRow = 0
enemiesColumn = 0
deadEnemyCounter = 0
#main game loop
while running:
   

    screen.fill("green")
     
    pygame.draw.rect(screen, THEME1[2] , playAreaRect)

    pressed = pygame.key.get_pressed() 
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
    xyEnemy , enemyDir = g.collisionEnemies(enemyXY,g.calculateXTopRight(enemyXY,enemySize,enemyDist),enemyDir,enemySize,enemyDist,enemyDead,playgroundSafeArea)


    g.makeEnemies(THEME1[3],enemyXY, enemySize, screen,enemyAlive ,enemyDist)

  


            
    if bulletHere:  #moves bullet if present and checks collision
        g.updateFire(THEME1[1],bulletXY,bulletSize,screen,bulletUp)
        bulletHere = g.detectCollisionEnemies(bulletXY,bulletSize,enemyXY,enemySize,enemyDist,enemyAlive)
        if not bulletHere:
            enemyDead = g.rowDead(enemyDead,enemyAlive)
            enemyLowest = g.updateLowest(enemyLowest,enemyAlive)
        if enemyDead[1] == 0: #victory condition
            running = False


    

    if bulletHere:
        bulletHere = g.detectCollisionBorder(bulletXY,bulletSize,DISPLAY_SIZE)


    counter += 1
    if counter == 1000:
        if bullet2Here and not bullet3Here:
            bullet3 , bullet3Here = g.enemyFire(enemyXY,enemyDist,enemySize,enemyLowest,bulletSize,THEME1[1],screen)
        elif bullet1Here and not bullet2Here:
            bullet2 , bullet2Here = g.enemyFire(enemyXY,enemyDist,enemySize,enemyLowest,bulletSize,THEME1[1],screen)
        elif not  bullet1Here:
            bullet1 , bullet1Here = g.enemyFire(enemyXY,enemyDist,enemySize,enemyLowest,bulletSize,THEME1[1],screen)
        counter = 0


# bullet events for enemies 
    if bullet1Here:
        bullet1 = g.updateFire(THEME1[1],bullet1,bulletSize,screen,0.2)
        bullet1Here = g.enemyBulletBorderCollision(bullet1, playgroundSafeArea)
        if running: #this is a lose condition with bullet collision
            running = g.collisionPlayerDeath(playerXY, playerSize, bullet1, bulletSize)

    if bullet2Here:
        bullet2 = g.updateFire(THEME1[1],bullet2,bulletSize,screen,0.2)
        bullet2Here = g.enemyBulletBorderCollision(bullet2, playgroundSafeArea)
        if running:
            running = g.collisionPlayerDeath(playerXY, playerSize, bullet2, bulletSize)

    if bullet3Here:
        bullet3 = g.updateFire(THEME1[1],bullet3,bulletSize,screen,0.2)
        bullet3Here = g.enemyBulletBorderCollision(bullet3, playgroundSafeArea)
        if running:
            running = g.collisionPlayerDeath(playerXY, playerSize, bullet3, bulletSize)



    #create player model and update movement
    playerXY = g.updatePlayerXY(playerXY, playerSize,pressed,DISPLAY_SIZE) 
    g.makeRect(THEME1[0],playerXY,playerSize,screen)

    #lose condition on enemy collision
    if g.gameOver(playerXY, xyEnemy, DISPLAY_SIZE, playerSize, (DISPLAY_SIZE[1] - playerXY[1] ) / playerSize[1], g.detectDeadRow(enemyAlive), enemyDist, enemySize):
        running = False
    
    pygame.display.flip()  

