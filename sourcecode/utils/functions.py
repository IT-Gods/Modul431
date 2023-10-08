import pygame
import random


#first implementation of classes for all rectangles
class Rectangle:


    def __init__(self ,x , y , xSize, ySize, color):
        self.coordinate = [x, y]
        self.size = [xSize, ySize]
        self.color = color
        self.alive = True
    
    
    def makeRect(self, screen):
        self.rect = pygame.Rect(self.coordinate[0],self.coordinate[1],self.size[0],self.size[1])
        pygame.draw.rect(screen,self.color,self.rect)

    def moveX(self, magnitude, direction, screen):
        self.coordinate[0] +=magnitude*direction
        self.makeRect(screen)


    def moveY(self, magnitude, direction, screen):
        self.coordinate[1] +=magnitude*direction
        self.makeRect(screen)




class Character(Rectangle):
    
    def __init__(self ,x , y , xSize, ySize, color):
        super().__init__(x , y , xSize, ySize, color)

    def fire1(self, xyBullet , xySizeBullet, colorBullet):
        self.bullet1 = Rectangle(xyBullet[0], xyBullet[1], xySizeBullet[0], xySizeBullet[1], colorBullet)

    def fire2(self, xyBullet , xySizeBullet, colorBullet):
        self.bullet2 = Rectangle(xyBullet[0], xyBullet[1], xySizeBullet[0], xySizeBullet[1], colorBullet)

    def fire3(self, xyBullet , xySizeBullet, colorBullet):
        self.bullet3 = Rectangle(xyBullet[0], xyBullet[1], xySizeBullet[0], xySizeBullet[1], colorBullet)


class Player(Character):
    def __init__(self ,x , y , xSize, ySize, color, lives):
        super().__init__(x , y , xSize, ySize, color)
        self.lives = lives
        self.coordinate = [x,y]
        self.size = [xSize, ySize]

    def calcMiddle(self, bulletSize):
        return [self.coordinate[0]+self.size[0]/2-(bulletSize[0]/2),self.coordinate[1]-self.size[1]/2]
    

    def movePlayer(self,pressed,displaySize, screen, borderMargin):
        if pressed[pygame.K_LEFT] and self.coordinate[0] != borderMargin[0]:
           return  self.moveX(0.5, -1, screen)
        if pressed[pygame.K_RIGHT] and self.coordinate[0] + self.size[1] != displaySize[0] - borderMargin[0]:
          return self.moveX(0.5, +1, screen)
        
    


class Enemies(Character):


    def __init__(self ,x , y , xSize, ySize, color):
        super().__init__(x , y , xSize, ySize, color)
        #i hate this definition make better if possible moray
        self.aliveIndividual = [[True, True, True, True],[True, True, True, True],[True, True, True, True],[True, True, True, True],[True, True, True, True],
                              [True, True, True, True],[True, True, True, True],[True, True, True, True],[True, True, True, True],[True, True, True, True]]
        self.shooterEnemy = [4,4,4,4,4,4,4,4,4,4]
        self.deadColumn = [0,9]
        self.deadRow = 4
        self.direction = 1

        self.dist = [self.size[0] / 1.2, self.size[1] / 1.2] 
    
    #this good
    def rowDead(self):
        counter = 0
        for row in range(len(self.aliveIndividual[self.deadRow])):
            if not self.aliveIndividual[self.deadRow][row]:
                counter += 1
        if counter == 10:
            self.deadRow -= 1

    #this also good
    def columnDead(self):
        counter = 0
        for i in range(len(self.aliveIndividual[self.deadColumn[0]])):
            if not self.aliveIndividual[self.deadColumn[0]][i]:
                counter += 1
        if counter == len(self.aliveIndividual[0]) and self.deadColumn[0] < 9:
            self.deadColumn[0] += 1
            
        counter = 0
        for i in range(len(self.aliveIndividual[self.deadColumn[1]])):
            if not self.aliveIndividual[self.deadColumn[1]][i]:
                counter += 1
        if counter == len(self.aliveIndividual[0]) and self.deadColumn[1] > 0:
            self.deadColumn[1] -= 1

    def topRight(self):
        arr = [self.coordinate[0] + (10 * self.size[0]) + (9 * self.dist[0]) ,self.coordinate[1]]
        return arr
     
    def collisionWall(self, safeArea):
        arr = self.topRight()
        if self.coordinate[0] + (self.size[0]+ self.dist[0])*self.deadColumn[0] < safeArea[0][0]:
            self.coordinate[1] += 10
            self.direction = 1
        elif arr[0] - (self.size[0]+ self.dist[0])*(9 - self.deadColumn[1]) > safeArea[1][0]:
            self.coordinate[1] += 10
            self.direction = -1

    def makeEnemies(self,screen):
            for enemiesRow in range(len(self.aliveIndividual)):
                for enemiesColumn in range(len(self.aliveIndividual[enemiesRow])):
                    if self.aliveIndividual[enemiesRow][enemiesColumn]:
                        self.makeRect(screen)
                    self.coordinate[1] += self.dist[1] + self.size[1]
                self.coordinate[0] += self.dist[0] + self.size[0] 
                self.coordinate[1] -= self.dist[1] * 4 + self.size[1] * 4  
            self.coordinate[0] -= self.dist[0] * 10 + self.size[0] * 10 
   
    def updateLowest(self):
            for enemiesRow in range(len(self.aliveIndividual)):
                x = 0
                for enemiesColumn in range(len(self.aliveIndividual[enemiesRow])):
                    if self.aliveIndividual[enemiesRow][enemiesColumn] and enemiesColumn + 1 > x:
                        x = enemiesColumn + 1
                        self.shooterEnemy[enemiesRow] = x

#select shooter enemy randomly
    def findShotPos(self):
        randomNum = random.randint(1,10)
        xy = [self.coordinate[0] + (randomNum - 1)*self.dist[0] +((randomNum)* self.size[0]) , self.coordinate[1] +(self.shooterEnemy[randomNum - 1] - 1)*self.dist[1] + (self.shooterEnemy[randomNum - 1]) * self.size[1]]
        return xy


















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
                        
                        
                
    return Tru
    








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





