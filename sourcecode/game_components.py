
def makeRect(THEME,XY,Size):
    playerRect = pygame.Rect(XY[0],XY[1],Size[0],Size[1])
    pygame.draw.rect(screen,THEME1[0],playerRect)



def updatePlayerXY(playerXY, playerSize)
    if pressed[pygame.K_LEFT] and playerXY[0] != 0:
        playerXY[0] -= 0.5
    if pressed[pygame.K_RIGHT] and playerXY[0] + playerSize[1] != DISPLAY_SIZE[0] :
        playerXY[0] += 0.5



