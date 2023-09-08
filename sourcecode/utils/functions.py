import pygame

<<<<<<< HEAD:sourcecode/utils/functions.py
def makeRect(theme,XY,Size,screen):
    playerRect = pygame.Rect(XY[0],XY[1],Size[0],Size[1])
    pygame.draw.rect(screen,theme[0],playerRect)
=======
#collection of functions used in the game

>>>>>>> fire:sourcecode/game_components.py


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


<<<<<<< HEAD:sourcecode/utils/functions.py
=======
#function to update fire and detect collision returns new coordinates of bullet
def updateFire(color,XY,sizeWH,screen):
    XY[1] -=1
    makeRect(color,XY,sizeWH,screen)

    return XY


def detectCollision(XY,sizeWH,screenSize):

    if XY[0] == 0 or XY[0] == screenSize[0]:
        return False
    elif XY[1] == 0 or XY[1] == screenSize[1]:
        return False
    else:
        return True


>>>>>>> fire:sourcecode/game_components.py
