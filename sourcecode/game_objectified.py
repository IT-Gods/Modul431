
#simple pygame initialisation will fill screen white
import pygame
import utils.coreModule as g
import utils.colors as c
import utils.helpers as h



def run_game(level, playerAmount, SPRITESTHEME1,screen):
    DISPLAY_SIZE = [1280,720]

    colorpalette = c.colors()
    pygame.init()
    clock = pygame.time.Clock()                         #time
    running = True                                      #this should be obvious



   #Carmen: Where is the menu and the settings? Should I not start with game_objectified?


    THEME1= [colorpalette.green(),colorpalette.red(),colorpalette.black(),colorpalette.white()]


    #definitions of ingame objects
    playerSize = [20,20]
    playerXY = [(DISPLAY_SIZE[0]-playerSize[0])/2,(DISPLAY_SIZE[1]*7/8)-playerSize[1]/2]


    bulletSize = [5,15]
    bulletXY = [playerXY[0]-playerSize[0]/2, playerXY[1]-playerSize[1]/2]
    bulletHere = False

    borderMargin = [20, 20]

    #Carmen: What is this used for?
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



    #INSHALLAH MAKE OBJECTS
    player1 = g.Player(playerXY[0],playerXY[1],playerSize[0],playerSize[1], SPRITESTHEME1[0], 3)
    player1.fire1(player1.calcMiddle(bulletSize),bulletSize,SPRITESTHEME1[1])
    player1.bullet1.alive = False
    if playerAmount == 2 :
        player2 = g.Player(playerXY[0],playerXY[1] + 50,playerSize[0],playerSize[1], SPRITESTHEME1[0], 3)
        player2.fire1(player2.calcMiddle(bulletSize),bulletSize,SPRITESTHEME1[1])
        player2.bullet1.alive = False
    enemy = g.Enemies(enemyXY[0],enemyXY[1],enemySize[0],enemySize[1],SPRITESTHEME1[1])
    enemy.fire1([1,1],[1,1],SPRITESTHEME1[2])
    enemy.fire2([1,1],[1,1],SPRITESTHEME1[2])
    enemy.fire3([1,1],[1,1],SPRITESTHEME1[2])
    enemy.bullet1.alive = False
    enemy.bullet2.alive = False
    enemy.bullet3.alive = False




    #main game loop
    while running:
       

        screen.fill("green")
         
        pygame.draw.rect(screen, THEME1[2] , playAreaRect)

        pressed = pygame.key.get_pressed() 
        for event in pygame.event.get():
            if pressed[pygame.K_ESCAPE]:                #if escape key pressed quit
                return -2
            if event.type == pygame.QUIT:
                return -2
            if pressed[pygame.K_SPACE]:                 #if spacebar is pressed make a bullet
                if player1.bullet1.alive == False:                 #checks if bullet on screen
                    player1.fire1(player1.calcMiddle(bulletSize),bulletSize,SPRITESTHEME1[2])
                    player1.bullet1.alive = True  
            if pressed[pygame.K_w] and playerAmount == 2:
                if player2.bullet1.alive == False:                 #checks if bullet on screen
                    player2.fire1(player2.calcMiddle(bulletSize),bulletSize,SPRITESTHEME1[2])
                    player2.bullet1.alive = True  

        enemy.moveXO(0.2 + (0.05 * (level -1)),enemy.direction)
        # found the bug this also draws a rect by default so make it seperately
        enemy.collisionWall(playgroundSafeArea)

        enemy.makeEnemies(screen)



                
        if player1.bullet1.alive:  #moves bullet if present and checks collision
            player1.bullet1.moveY(-1,1,screen)
            player1.bullet1.alive = h.detectCollisionEnemies(player1.bullet1.coordinate,player1.bullet1.size,enemy.coordinate,enemy.size,enemy.dist,enemy.aliveIndividual)
            if not player1.bullet1.alive:
                enemy.rowDead()
                enemy.columnDead()
                enemy.updateLowest()
        if playerAmount == 2:
                    
            if player2.bullet1.alive:  #moves bullet if present and checks collision
                player2.bullet1.moveY(-1,1,screen)
                player2.bullet1.alive = h.detectCollisionEnemies(player2.bullet1.coordinate,player2.bullet1.size,enemy.coordinate,enemy.size,enemy.dist,enemy.aliveIndividual)
                if not player1.bullet1.alive:
                    enemy.rowDead()
                    enemy.columnDead()
                    enemy.updateLowest() 

                #Carmen: what is Enemy dead?
            if enemyDead[1] == 0: #victory condition
                running = False


        

        if player1.bullet1.alive:
            player1.bullet1.alive = h.detectCollisionBorder(player1.bullet1.coordinate,DISPLAY_SIZE)
        if playerAmount == 2:
            if player2.bullet1.alive:
                player2.bullet1.alive = h.detectCollisionBorder(player2.bullet1.coordinate,DISPLAY_SIZE)

    #FIXED TILL HERE I GUESS
    #I WANT TO DIE
        counter += 1
        if counter == 1000:
        
            if enemy.bullet2.alive and not enemy.bullet3.alive:
                enemy.fire3(enemy.findShotPos(),bulletSize,SPRITESTHEME1[2])
            elif enemy.bullet1.alive and not enemy.bullet2.alive:
                    enemy.fire2(enemy.findShotPos(),bulletSize,SPRITESTHEME1[2])
            elif not  enemy.bullet1.alive:
                enemy.fire1(enemy.findShotPos(),bulletSize,SPRITESTHEME1[2])
            counter = 0


    # bullet events for enemies 
    #Carmen: Am I correct in assuming this is the enemies firing bullets?
        if enemy.bullet1.alive:
            enemy.bullet1.moveY(1,0.2,screen)
            enemy.bullet1.alive = h.enemyBulletBorderCollision(enemy.bullet1.coordinate, playgroundSafeArea)
            if h.collisionRect(enemy.bullet1.coordinate,enemy.bullet1.size,player1.coordinate,player1.size):
                player1.lives -= 1
                enemy.bullet1.alive = False
            #if running: #this is a lose condition with bullet collision FIX LATER PLS TY <3
                #running = g.collisionPlayerDeath(playerXY, playerSize, bullet1, bulletSize)

        if enemy.bullet2.alive:
            enemy.bullet2.moveY(1,0.2,screen)
            enemy.bullet2.alive = h.enemyBulletBorderCollision(enemy.bullet2.coordinate, playgroundSafeArea)
            if h.collisionRect(enemy.bullet2.coordinate,enemy.bullet2.size,player1.coordinate,player1.size):
                player1.lives -= 1
                enemy.bullet2.alive = False

        if enemy.bullet3.alive:
            enemy.bullet3.moveY(1,0.2,screen)
            enemy.bullet3.alive = h.enemyBulletBorderCollision(enemy.bullet3.coordinate, playgroundSafeArea)
            if h.collisionRect(enemy.bullet3.coordinate,enemy.bullet3.size,player1.coordinate,player1.size):
                player1.lives -= 1
                enemy.bullet3.alive = False

        #create player model and update movement
        player1.makeRect(screen)
        player1.movePlayer(pressed[pygame.K_LEFT],pressed[pygame.K_RIGHT],DISPLAY_SIZE, screen,borderMargin)
        if playerAmount == 2:
            player2.makeRect(screen)
            player2.movePlayer(pressed[pygame.K_a],pressed[pygame.K_d],DISPLAY_SIZE, screen,borderMargin)
        #lose condition on enemy collision
        if h.gameOver( enemy.coordinate, DISPLAY_SIZE, playerSize,enemy.deadRow , enemyDist, enemySize):
            running = False
            return -1
        if player1.lives == 0:
            running = False

            return -1
        if h.victory(enemy.aliveIndividual):
            return 1

        pygame.display.flip()  
       
