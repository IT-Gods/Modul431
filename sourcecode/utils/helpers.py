import pygame

#what is this function?
def detectCollisionBorder(XY,screenSize):

    if XY[0] == 0 or XY[0] == screenSize[0]:
        return False
    elif XY[1] == 0 or XY[1] == screenSize[1]:
        return False
    else: 
        return True


#collision detection for enemies and player bullets
def detectCollisionEnemies(XYBullet,sizeBullet,XYEnemy,sizeEnemy,distEnemy,aliveEnemy):
    for column in range(len(aliveEnemy)):
        for row in range(len(aliveEnemy[column])):
            if aliveEnemy[column][row]:
                if XYBullet[0] > (XYEnemy[0] + sizeEnemy[0]*column + distEnemy[0]*column)-sizeBullet[0] and XYBullet[0] < (XYEnemy[0] + sizeEnemy[0]*(column + 1) + distEnemy[0]*column):
                    if XYBullet[1] > (XYEnemy[1] + sizeEnemy[1]*row + distEnemy[1]*row) and XYBullet[1] < (XYEnemy[1] + sizeEnemy[1]*row + distEnemy[1]*(row + 1)):
                        aliveEnemy[column][row] = False

                        return False
                        
                        

    








#function keeps track of how many column of enemies are alive
def columnDead(deadEnemy,aliveEnemy):
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




#Standard function for detecting collision between two rectangles
#objects should be 2x1 array in following order 
#(coordinate1, size1 ,coordinate2, size2) 
def collisionRect(xyObject1,sizeObject1, xyObject2, sizeObject2 ):
    if xyObject2[0] > (xyObject1[0])-sizeObject2[0] and xyObject2[0] < (xyObject1[0]+ sizeObject1[0]):
        if xyObject2[1] > (xyObject1[1])-sizeObject2[1] and xyObject2[1] < (xyObject1[1]+ sizeObject1[1]):
            return True
    return False


def detectDeadRow(enemyAlive):
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


def enemyBulletBorderCollision(xyBullet,screenSize):
    if xyBullet[1] > screenSize[1][1] - screenSize[0][1]:
        return False
    else:
        return True