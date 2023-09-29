import pygame
import random

#collection of functions used in the game



#create a rectangle is used as filler for models
def makeRect(color,XY,sizeWH,screen):
    myRect = pygame.Rect(XY[0],XY[1],sizeWH[0],sizeWH[1])
    pygame.draw.rect(screen,color,myRect)


#function to update player movement
def updatePlayerXY(playerXY, playerSize,pressed,displaySize):
    if pressed[pygame.K_LEFT] and playerXY[0] != 0:
        playerXY[0] -= 0.5
    if pressed[pygame.K_RIGHT] and playerXY[0] + playerSize[1] != displaySize[0] :
        playerXY[0] += 0.5
    return playerXY



#function to update fire and detect collision returns new coordinates of bullet
def updateFire(color,XY,sizeWH,screen,direction):
    XY[1] +=1*direction
    makeRect(color,XY,sizeWH,screen)
    return XY


def detectCollisionBorder(XY,sizeWH,screenSize):

    if XY[0] == 0 or XY[0] == screenSize[0]:
        return False
    elif XY[1] == 0 or XY[1] == screenSize[1]:
        return False
    else: 
        return True

def detectCollisionEnemies(XYBullet,sizeBullet,XYEnemy,sizeEnemy,distEnemy,aliveEnemy):
    for column in range(len(aliveEnemy)):
        for row in range(len(aliveEnemy[column])):
            if aliveEnemy[column][row]:
                if XYBullet[0] > (XYEnemy[0] + sizeEnemy[0]*column + distEnemy[0]*column)-sizeBullet[0] and XYBullet[0] < (XYEnemy[0] + sizeEnemy[0]*(column + 1) + distEnemy[0]*column):
                    if XYBullet[1] > (XYEnemy[1] + sizeEnemy[1]*row + distEnemy[1]*row) and XYBullet[1] < (XYEnemy[1] + sizeEnemy[1]*row + distEnemy[1]*(row + 1)):
                        aliveEnemy[column][row] = False

                        return False
                        
                        
                
    return True

def makeEnemies(color,XY,sizeWH,screen, arr, dist):
    for enemiesRow in range(len(arr)):
        for enemiesColumn in range(len(arr[enemiesRow])):
            if arr[enemiesRow][enemiesColumn]:
                makeRect(color, XY , sizeWH, screen)
            XY[1] += dist[1] + sizeWH[1]
        XY[0] += dist[0] + sizeWH[0] 
        XY[1] -= dist[1] * 4 + sizeWH[1] * 4  
    XY[0] -= dist[0] * 10 + sizeWH[0] * 10 


def calculateXTopRight(XY,enemySize, enemyDist):
   firstElement = XY[0] + (10 * enemySize[0]) + (9 * enemyDist[0]) 
   secondElement = XY[1]
   return [firstElement, secondElement]     #i dont like how this is returned

def moveEnemiesX(xyEnemies, directionEnemies):
    xyEnemies[0] += 0.2*directionEnemies     
    return xyEnemies

def collisionEnemies(xyEnemies,xyTopRight,enemyDir,sizeEnemy,distEnemy,deadEnemy, safeArea):
    if xyEnemies[0] + (sizeEnemy[0]+distEnemy[0])*deadEnemy[0] < safeArea[0][0] - 5:
        xyEnemies[1] += 10
        enemyDir = 1
    elif xyTopRight[0] - (sizeEnemy[0]+distEnemy[0])*(10 -deadEnemy[1]) > safeArea[1][0] - (safeArea[0][0] - 5):
        xyEnemies[1] += 10
        enemyDir = -1
    return xyEnemies , enemyDir

def rowDead(deadEnemy,aliveEnemy):
    counter = 0
    for i in range(0,len(aliveEnemy[deadEnemy[0]-1])):
        if not aliveEnemy[deadEnemy[0]][i]:
            counter += 1
    if counter == 4 and deadEnemy[0] < 9:
        deadEnemy[0] += 1
        
    counter = 0
    for i in range(0,len(aliveEnemy[deadEnemy[1]-1])):
        if not aliveEnemy[deadEnemy[1]-1][i]:
            counter += 1
    if counter == 4 and deadEnemy[1] > 0:
        deadEnemy[1] -= 1
    return deadEnemy

def gameOver(playerXY, enemyXY, displayXY, playerSize, playerContainerScope,enemyDeadCounter, enemyDist, enemySize):
    playerZone = displayXY[1] / 2 - (displayXY[1] - playerXY[1])  + playerContainerScope * playerSize[1]

    if enemyDeadCounter >= 1:
       return enemyXY[1] -  ((enemyDeadCounter * (enemySize[1] + enemyDist[1]) ) ) >  playerZone - playerSize[1]
    else:
       return enemyXY[1] >  playerZone - playerSize[1]


def detectDeadRow(enemyAlive):
      counter = 0
      for row in range(len(enemyAlive)):
        for column in range(len(enemyAlive[row])):
            if not enemyAlive[row][column]:
              counter += 1
        return counter   



def updateLowest(lowestEnemy,aliveEnemy):
    for enemiesRow in range(len(aliveEnemy)):
        x = 0
        for enemiesColumn in range(len(aliveEnemy[enemiesRow])):
            if aliveEnemy[enemiesRow][enemiesColumn] and enemiesColumn + 1 > x:
                x = enemiesColumn + 1
                lowestEnemy[enemiesRow] = x
    return lowestEnemy

def enemyFire(xyEnemy,distEnemy,sizeEnemy,lowestEnemy,sizeBullet,color,screen):
    randomNum = random.randint(1,10)
    xy = [xyEnemy[0] + (randomNum - 1)*distEnemy[0] +((randomNum)* sizeEnemy[0]) , xyEnemy[1] +(lowestEnemy[randomNum - 1] - 1)*distEnemy[1] + (lowestEnemy[randomNum - 1]) * sizeEnemy[1]]
    makeRect(color ,xy ,sizeBullet,screen)
    return xy , True

def enemyBulletBorderCollision(xyBullet,screenSize):
    if xyBullet[1] > screenSize[1]:
        return False
    else:
        return True





