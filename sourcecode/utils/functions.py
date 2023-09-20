import pygame
import re

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


def detectCollision(XY,sizeWH,screenSize):

    if XY[0] == 0 or XY[0] == screenSize[0]:
        return False
    elif XY[1] == 0 or XY[1] == screenSize[1]:
        return False
    else: 
        return True


def makeEnemies(color,XY,sizeWH,screen, arr, dist):
    for enemiesRow in range(len(arr)):
        for enemiesColumn in range(len(arr[enemiesRow])):
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

def collisionEnemies(xyEnemies,xyTopRight,displaySize,enemyDir):
    if xyEnemies[0] < 5:
        xyEnemies[1] += 10
        enemyDir = 1
    elif xyTopRight[0] > displaySize[0] - 5:
        xyEnemies[1] += 10
        enemyDir = -1
    return xyEnemies , enemyDir


