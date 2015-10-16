from pyprocessing import *
import random

cells = []

class Cell():
    def __init__(self,x,y,state):
        self.x = x
        self.y = y
        self.state = state
        self.adjacent = []

    def getAdjacents(self):
        topLeft = None
        midLeft = None
        lowLeft = None
        topMid = None
        lowMid = None
        topRight = None
        midRight = None
        lowRight = None
        for cell in cells:
            if self.x-1 == cell.x:
                if self.y-1 == cell.y:
                    topLeft = cell
                if self.y == cell.y:
                    midLeft = cell
                if self.y+1 == cell.y:
                    lowLeft = cell
            if self.x == cell.x:
                if self.y-1 == cell.y:
                    topMid = cell
                if self.y+1 == cell.y:
                    lowMid = cell
            if self.x+1 == cell.x:
                if self.y-1 == cell.y:
                    topRight = cell
                if self.y == cell.y:
                    midRight = cell
                if self.y+1 == cell.y:
                    lowRight = cell
        self.adjacent = [topLeft,midLeft,lowLeft,topMid,lowMid,topRight,midRight,lowRight]

    def changeState(self):
        alive = 0
        self.getAdjacents()
        for cell in self.adjacent:
            if cell != None:
                if cell.state == 1:
                    alive += 1
        if self.state == 1:
            #underpopulation
            if alive < 2:
                self.state = 0
            #alive...for now
            if alive == 2 or alive == 3:
                self.state = 1 #unnecessary line
            #overcrowding
            if alive > 3:
                self.state = 0
        else:
            #reproduction
            if alive == 3:
                self.state = 1

def setup():
    size(550,550)
    ellipseMode(CENTER)
    noStroke()
    for x in range(550):
        for y in range(550):
            newCell = Cell(x,y,0)
            cells.append(newCell)

    #setup animation
    for cell in cells:
        if cell.x == 225:
            if cell.y == 225:
                cell.state = 1
            if cell.y == 224:
                cell.state = 1
            if cell.y == 223:
                cell.state = 1
        if cell.x == 224:
            if cell.y == 225:
                cell.state = 1
            if cell.y == 224:
                cell.state = 1
            if cell.y == 223:
                cell.state = 1

def draw():
    fill(200,50)
    rect(0,0,550,550)
    fill(0)
    for cell in cells:
        cell.changeState()
        #update cell state
        if cell.state == 0: #dead
            fill(0,0,0)
            rect(cell.x,cell.y,1,1)
        else: #alive
            #rand1 = random.randint(0,255)
            #rand2 = random.randint(0,255)
            #rand3 = random.randint(0,255)
            #fill(rand1,rand2,rand3)
            fill(255,255,255)
            rect(cell.x,cell.y,1,1)

run()