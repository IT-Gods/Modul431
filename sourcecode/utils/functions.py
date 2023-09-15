import pygame

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
            makeRect(color, XY , sizeWH, screen)
            XY[1] += dist[1] + sizeWH[1]
        XY[0] += dist[0] + sizeWH[0]
        XY[1] -= dist[1] * 4 + sizeWH[1] * 4
    XY[0] -= dist[0] * 10 + sizeWH[0] * 10

