import pygame


def makeRect(color,XY,SizeWH,screen):
    playerRect = pygame.Rect(XY[0],XY[1],Size[0],Size[1])
    pygame.draw.rect(screen,color,playerRect)



def updatePlayerXY(playerXY, playerSize,displaySize):
    pressed= pygame.key.get_pressed()
    if pressed[pygame.K_LEFT] and playerXY[0] != 0:
        playerXY[0] -= 0.5
    if pressed[pygame.K_RIGHT] and playerXY[0] + playerSize[1] != displaySize[0] :
        playerXY[0] += 0.5



