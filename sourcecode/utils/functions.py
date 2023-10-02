import pygame
import random

#first implementation of classes for all rectangles
class Rectangle:
    
    



    def __init__(self ,x , y , xSize, ySize, color):
        self.coordinate = [x, y]
        self.size = [xSize, ySize]
        self.color = color
        self.alive = True
    
    
    def makeRect(self):
        self.rect = pygame.Rect(self.coordinate[0],self.coordinate[1],self.sizesize[0],self.size[1])
        pygame.draw.rect(screen,self.color,self.rect)

    def moveX(self, magnitude, direction):
        self.coordinate[0] +=magnitude*direction
        self.rect = pygame.Rect(self.coordinate[0],self.coordinate[1],self.sizesize[0],self.size[1])
        pygame.draw.rect(screen,self.color,self.rect)


    def moveY(self, magnitude, direction):
        self.coordinate[1] +=magnitude*direction
        self.rect = pygame.Rect(self.coordinate[0],self.coordinate[1],self.sizesize[0],self.size[1])
        pygame.draw.rect(screen,self.color,self.rect)




class Character(Rectangle):
    

    def __init__(self ,x , y , xSize, ySize, color):
        super().__init__(x , y , xSize, ySize, color)


    def fire(self, xyBullet , xySizeBullet, colorBullet):
        self.bullet = Rectangle(xyBullet[0], xyBullet[1], xySizeBullet[0], xySizeBullet[1], colorBullet)


class Player(Character):
    def __init__(self ,x , y , xSize, ySize, color, lives):
        super().__init__(x , y , xSize, ySize, color)
        self.lives = lives


    def calcMiddle(self, bulletSize):
        return [self.coordinate[0]+self.size[0]/2-(bulletSize[0]/2),self.coordinate[1]-self.size[1]/2]
    





class Enemies(Character):


    def __init__(self ,x , y , xSize, ySize, color):
        super().__init__(x , y , xSize, ySize, color)
        #i hate this definition make better if possible moray
        self.aliveInividual = [[True, True, True, True],[True, True, True, True],[True, True, True, True],[True, True, True, True],[True, True, True, True],
                              [True, True, True, True],[True, True, True, True],[True, True, True, True],[True, True, True, True],[True, True, True, True]]
        self.shooterEnemy = [4,4,4,4,4,4,4,4,4,4]
        self.deadColumn = [0,9]
        self.deadRow = 0
        self.direction = 1

        self.dist = [self.size[0] / 1.2, self.size[1] / 1.2] 
    
    #this good
    def rowDead(self):
        currRow = len(self.aliveIndividual[0]) - self.deadRow -1
        for row in range(len(enemyAlive[column]-1)):
            if not self.aliveIndividual[column][currRow]:
                self.deadRow += 1
    #this also good
    def columnDead(self):
        counter = 0
        for i in range(len(self.aliveIndividual[self.deadColumn[0]])):
            if not self.aliveIndividual[self.deadColumn[0]][i]:
                counter += 1
        if counter == len(self.aliveIndividual[0]) and self.deadColumn[0] < 9:
            deadEnemy[0] += 1
            
        counter = 0
        for i in range(len(self.aliveIndividual[self.deadColumn[1]])):
            if not self.aliveIndividual[self.deadColumn[1]][i]:
                counter += 1
        if counter == len(self.aliveIndividual[0]) and self.deadColumn[1] > 0:
            deadEnemy[1] -= 1
     
    #i am too monkey rn to check if this is good
    def collisionWall(self, safeArea):
        xyTopRight[0] = self.coordinate[0] + (10 * self.size[0]) + (9 * enemyDist[0]) 
        xyTopRight[1] = XY[1]


        if self.coordinates[0] + (self.size[0]+ self.dist[0])*self.deadColumn[0] < safeArea[0][0]:
            self.coordinates[1] += 10
            self.direction = 1
        elif xyTopRight[0] - (self.size[0]+ self.dist[0])*(10 -self.deadColumn[1]) > safeArea[1][0] - (safeArea[0][0]):
            self.coordinates[1] += 10
            self.direction = -1


        #shit is now fixed
        def makeEnemies(self):
            for enemiesRow in range(len(arr)):
                for enemiesColumn in range(len(self.aliveIndividual[enemiesRow])):
                    if self.aliveIndividual[enemiesRow][enemiesColumn]:
                        self.makeRect(self)
                    self.coordinate[1] += self.dist[1] + self.size[1]
                self.coordinate[0] += self.dist[0] + self.size[0] 
                self.coordinate[1] -= self.dist[1] * 4 + self.size[1] * 4  
            self.coordinate[0] -= self.dist[0] * 10 + self.size[0] * 10 

# moray you fucking ape this is ineffiecient just check lowest enemies
        def updateLowest(self,lowestEnemy,aliveEnemy):
            for enemiesRow in range(len(self.aliveIndividual)):
                x = 0
                for enemiesColumn in range(len(self.aliveIndividual[enemiesRow])):
                    if self.aliveIndividual[enemiesRow][enemiesColumn] and enemiesColumn + 1 > x:
                        x = enemiesColumn + 1
                        self.shooterEnemy[enemiesRow] = x

#add some random function for shooting or some shit just make it work



#collection of functions used in the game
#half of these will need to be deleted if possible only leave collision



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





def detectCollisionBorder(XY,sizeWH,screenSize):

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

#funtion for controlling whether enemies hit a wall and change direction based on 
#which wall was hit
def collisionEnemies(xyEnemies,xyTopRight,enemyDir,sizeEnemy,distEnemy,deadEnemy, safeArea):
    if xyEnemies[0] + (sizeEnemy[0]+distEnemy[0])*deadEnemy[0] < safeArea[0][0] - 5:
        xyEnemies[1] += 10
        enemyDir = 1
    elif xyTopRight[0] - (sizeEnemy[0]+distEnemy[0])*(10 -deadEnemy[1]) > safeArea[1][0] - (safeArea[0][0] - 5):
        xyEnemies[1] += 10
        enemyDir = -1
    return xyEnemies , enemyDir


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

def gameOver(playerXY, enemyXY, displayXY, playerSize, playerContainerScope,enemyDeadCounter, enemyDist, enemySize):
    playerZone = displayXY[1] / 2 - (displayXY[1] - playerXY[1])  + playerContainerScope * playerSize[1]

    if enemyDeadCounter >= 1:
       return enemyXY[1] -  ((enemyDeadCounter * (enemySize[1] + enemyDist[1]) ) ) >  playerZone - playerSize[1]
    else:
       return enemyXY[1] >  playerZone - playerSize[1]

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

def enemyFire(xyEnemy,distEnemy,sizeEnemy,lowestEnemy,sizeBullet,color,screen):
    randomNum = random.randint(1,10)
    xy = [xyEnemy[0] + (randomNum - 1)*distEnemy[0] +((randomNum)* sizeEnemy[0]) , xyEnemy[1] +(lowestEnemy[randomNum - 1] - 1)*distEnemy[1] + (lowestEnemy[randomNum - 1]) * sizeEnemy[1]]
    makeRect(color ,xy ,sizeBullet,screen)
    return xy , True

def enemyBulletBorderCollision(xyBullet,screenSize):
    if xyBullet[1] > screenSize[1][1] - screenSize[0][1]:
        return False
    else:
        return True





