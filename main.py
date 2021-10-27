import random
import numpy as np
class Game:
    def __init__(self):
        self.matrix = [[0 for _ in range(4)] for _ in range(4)]

    def create_game(self):
        count = 0
        while count < 2:
            x,y = random.sample([0,0,1,1,2,2,3,3],2)
            if self.matrix[x][y] == 0:
                self.matrix[x][y] = 2
                count +=1

    def col(self, num):
        return [self.matrix[i][num] for i in range(len(self.matrix))[::-1]] #makes a row from a column, left to right
    def transpose(self):
        returnMatrix = []
        for i in range(4):
            returnMatrix.append([])
            for j in range(4):
                returnMatrix[i].append(self.matrix[j][i])
        self.matrix = returnMatrix
        
    def pushRight(self):
        for rowNum in range(4):
                row = self.matrix[rowNum]
                mergeFlag = False
                for i in range(4)[::-1]:
                    try:
                        pushIndex = i
                        while pushIndex<4:
                            if row[pushIndex+1] == 0:
                                row[pushIndex+1] += row[pushIndex]
                                row[pushIndex] = 0
                                pushIndex += 1
                            elif row[pushIndex+1] == row[pushIndex] and not mergeFlag:
                                row[pushIndex+1] += row[pushIndex]
                                row[pushIndex] = 0
                                pushIndex += 1
                                mergeFlag=True
                            else:
                                break
                    except:
                        continue
                for i in range(4):
                    self.matrix[rowNum][i] = row[i]
        for i in range(4): #update
            for j in range(4):
                try:
                    if self.matrix[i][j] == 0 and self.matrix[i-1][j] != 0:
                        self.matrix[i][j] = 2
                        return
                except:
                    continue
    def pushLeft(self):
        for rowNum in range(4): #push
                row = self.matrix[rowNum]
                mergeFlag = False
                for i in range(4):
                    try:
                        pushIndex = i
                        while pushIndex>0:
                            if row[pushIndex-1] == 0:
                                row[pushIndex-1] += row[pushIndex]
                                row[pushIndex] = 0
                                pushIndex -= 1
                            elif row[pushIndex-1] == row[pushIndex] and not mergeFlag:
                                row[pushIndex-1] += row[pushIndex]
                                row[pushIndex] = 0
                                pushIndex -= 1
                                mergeFlag=True
                            else:
                                break
                    except:
                        continue
                for i in range(4):
                    self.matrix[rowNum][i] = row[i]
        for i in range(4): #update
            for j in range(4):
                try:
                    if self.matrix[i][j] == 0 and self.matrix[i+1][j] != 0:
                        self.matrix[i][j] = 2
                        return
                except:
                    continue
    def pushUp(self):
        self.transpose()
        for colNum in range(4):
            row = self.matrix[colNum]
            mergeFlag = False
            for i in range(4):#push left
                try:
                    pushIndex = i
                    while pushIndex>0:
                        if row[pushIndex-1] == 0:
                            row[pushIndex-1] += row[pushIndex]
                            row[pushIndex] = 0
                            pushIndex -= 1
                        elif row[pushIndex-1] == row[pushIndex] and not mergeFlag:
                            row[pushIndex-1] += row[pushIndex]
                            row[pushIndex] = 0
                            pushIndex -= 1
                            mergeFlag=True
                        else:
                            break
                except:
                    continue
            for i in range(4):
                self.matrix[i][colNum] = row[i] #update the values in the matrix
            self.pushLeft()
            self.transpose()
            for i in range(4): #update
                for j in range(4):
                    try:
                        if self.matrix[i][j] == 0 and self.matrix[i][j-1] != 0:
                            self.matrix[i][j] = 2
                            return
                    except:
                        continue

    def pushDown(self):
           for colNum in range(4):
                row = self.col(colNum)
                mergeFlag = False
                for i in range(4)[::-1]: #push right
                    try:
                        pushIndex = i
                        while pushIndex<4:
                            if row[pushIndex+1] == 0:
                                row[pushIndex+1] += row[pushIndex]
                                row[pushIndex] = 0
                                pushIndex += 1
                            elif row[pushIndex+1] == row[pushIndex] and not mergeFlag:
                                row[pushIndex+1] += row[pushIndex]
                                row[pushIndex] = 0
                                pushIndex += 1
                                mergeFlag=True
                            else:
                                break
                    except:
                        continue
                
                for i in range(4):
                    self.matrix[i][colNum] = row[i] #update the values in the matrix
                for i in range(4): #update
                    for j in range(4):
                        try:
                            if self.matrix[i][j] == 0 and self.matrix[i][j+1] != 0:
                                self.matrix[i][j] = 2
                                return
                        except:
                            continue

    def move(self,move):
        if move == "r":
            print("right")
            self.pushRight()
        elif move == "l":
            print("left")
            self.pushLeft()
        elif move == "u":
            print("up")
            self.pushUp()
        else:
            print("down")
            self.pushDown()

    def checkLose(self):
        for i in range(4):
            for j in range(4):
                try:
                    current = self.matrix[i][j]
                    if current == self.matrix[i-1][j] or current == self.matrix[i][j-1] or current == self.matrix[i+1][j] or current == self.matrix[i][j+1] or current == 0:
                        return False
                except:
                    continue
        return True

    def update(self):
        rows = list(range(4))
        random.shuffle(rows)
        for i in rows:
            random.shuffle(rows)
            for j in rows:
                if self.matrix[i][j] == 0:
                    self.matrix[i][j] = 2
                    return
    def mainPlay(self):
        self.create_game()
        while not self.checkLose():
            print(np.matrix(self.matrix))
            self.move(input("enter your move: "))


#if you want to play, uncomment these lines of code
#g = Game()
#g.mainPlay()
