#import keyboard
import random
from color import printcol
import time
import keyboard
import os
"""
shot_pressed = 0
was_pressed = False

x = 0

while True:
    #print(x)
    if keyboard.is_pressed('s'):
        x = 1
        if not was_pressed:
            shot_pressed += 1
            print("shot_pressed %d times"%shot_pressed)
            was_pressed = True
    else:
        x = 0
        was_pressed = False
"""

def directionUp(dire):
    if dire == "up":
        return (0,-1)
    elif dire == "down":
        return (0,1)
    elif dire == "left":
        return (-1,0)
    if dire == "right":
        return (1,0)

class Snake:
    def __init__(self,n):
        self.n = n
        self.board = [[0 for i in range(n)] for i in range(n)]
        self.snake = [(int(n/2),int(n/2))]
        self.points = 0
        self.fruit = []
        self.direction = "up"
        self.poison = []

    def printboard(self):
        self.board = [[0 for i in range(self.n)] for i in range(self.n)]
        for sn in self.snake:
            x,y = sn
            self.board[y][x] = 1

        for fr in self.fruit:
            x,y = fr
            self.board[y][x] = 2
        
        for po in [poi[0] for poi in self.poison]:
            x,y = po
            self.board[y][x] = 3

        for row in self.board:
            for ele in row:
                if ele == 0:
                    print("▓",end = " ")
                elif ele == 1:
                    printcol("▓","green")
                elif ele == 2:
                    printcol("▓","yellow")
                elif ele == 3:
                    printcol("▓","purple")
            print()

    def move(self):
        headx,heady = self.snake[0]
        direx,direy = directionUp(self.direction)
        if (headx + direx , heady + direy) in self.snake:
            return False

        if (headx + direx , heady + direy) in [poi[0] for poi in self.poison]:
            return False

        elif (headx + direx , heady + direy) in self.fruit:
            self.snake = [(headx + direx , heady + direy)] + self.snake
            self.fruit.remove((headx + direx , heady + direy))
            self.points += 1 
            return True

        else:
            if headx + direx >= self.n:
                headx = - 1  
            if headx + direx <= -1:
                headx = self.n

            if heady + direy >= self.n:
                heady = - 1  
            if heady + direy <= -1:
                heady = self.n  

            lastx , lasty = self.snake[-1]
            self.snake = [(headx + direx , heady + direy)] + self.snake[:-1]
            self.board[lasty][lastx] = 0
            return True

    def randomFruit(self):
        while len(self.fruit) < 4:
            newFruit = (random.randint(1,self.n-2),random.randint(1,self.n-2))
            while newFruit in self.snake:
                newFruit = (random.randint(1,self.n-2),random.randint(1,self.n-2))
            self.fruit.append(newFruit)

    def randomPoison(self):
        while len(self.poison) < int(self.points/5):
            newPoison = (random.randint(1,self.n-2),random.randint(1,self.n-2))
            life = random.randint(10,100)
            while newPoison in self.snake or newPoison in self.forbidenPos(self.snake[0]):
                newPoison = (random.randint(1,self.n-2),random.randint(1,self.n-2))
            self.poison.append([newPoison,life])

    def forbidenPos(self,head):
        if self.direction == "up":
            return [(head[0],i) for i in range(0, head[1])]
        elif self.direction == "down":
            return [(head[0],i) for i in range(head[1] + 1 , self.n)]
        elif self.direction == "left":
            return [(i,head[1]) for i in range(0, head[0])]
        if self.direction == "right":
            return [(i,head[1]) for i in range(head[0] + 1, self.n)]

    def updateLife(self):
        for poi in self.poison:
            if poi[1] > 0:
                poi[1] -= 1
            else:
                self.poison.remove(poi)



    
A = Snake(20)
A.randomFruit()
A.randomPoison()
A.updateLife()
A.printboard()
A.direction = "up"
res = A.move()
while res:
    A.randomFruit()
    A.randomPoison()
    A.updateLife()
    print("\n")
    print("Points = " + str(A.points))
    print("\n")
    A.printboard()
    if keyboard.is_pressed('z'):
        if A.direction != "down":
            A.direction = "up"
    elif keyboard.is_pressed('q'):
        if A.direction != "right":    
            A.direction = "left"
    elif keyboard.is_pressed('s'):
        if A.direction != "up":    
            A.direction = "down"
    elif keyboard.is_pressed('d'):
        if A.direction != "left":
            A.direction = "right"
    elif keyboard.is_pressed('k'):
        break
    time.sleep(0.08)
    res = A.move()
    print("\n")
    os.system("clear")


A.printboard()
print("\nYou die\n")
print("Points = "+str(A.points) +"\ns")