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
            #overcrowding
            elif alive > 3:
                self.state = 0
            #alive...for now
            else:
                self.state = 1 #unnecessary line
        else:
            #reproduction
            if alive == 3:
                self.state = 1

def setup():
    #print "ran setup"
    size(800,800)
    #ellipseMode(CENTER)
    noStroke()
    for x in range(50):
        for y in range(50):
            #randState = random.randint(0,1)
            #newCell = Cell(x,y,randState)
            newCell = Cell(x,y,0)
            cells.append(newCell)

    #setup animation
    '''
    for cell in cells:
        if cell.x == 25:
            if cell.y == 26:
                cell.state = 1
            if cell.y == 25:
                cell.state = 1
            if cell.y == 24:
                cell.state = 1
        elif cell.x == 24:
            if cell.y == 25:
                cell.state = 1
        elif cell.x == 26:
            if cell.y == 24:
                cell.state = 1
    '''
    #Diehard
    '''
    for cell in cells:
        if cell.y == 24:
            if cell.x == 16:
                cell.state = 1
        elif cell.y == 25:
            if cell.x == 10:
                cell.state = 1
            if cell.x == 11:
                cell.state = 1
        elif cell.y == 26:
            if cell.x == 11:
                cell.state = 1
            if cell.x == 15:
                cell.state = 1
            if cell.x == 16:
                cell.state = 1
            if cell.x == 17:
                cell.state = 1
    '''
    for cell in cells:
        if cell.y == 23:
            if cell.x == 23:
                cell.state = 1
            elif cell.x == 24:
                cell.state = 1
            elif cell.x == 25:
                cell.state = 1
            elif cell.x == 27:
                cell.state = 1
        elif cell.y == 24:
            if cell.x == 23:
                cell.state = 1
        elif cell.y == 25:
            if cell.x == 26:
                cell.state = 1
            elif cell.x == 27:
                cell.state = 1
        elif cell.y == 26:
            if cell.x == 24:
                cell.state = 1
            elif cell.x == 25:
                cell.state = 1
            elif cell.x == 27:
                cell.state = 1
        elif cell.y == 27:
            if cell.x == 23:
                cell.state = 1
            elif cell.x == 25:
                cell.state = 1
            elif cell.x == 27:
                cell.state = 1

def draw():
    #print "ran draw"
    fill(200,50)
    rect(0,0,500,500)
    fill(0)
    alive = 0
    for cell in cells:
        if cell.state == 0: #dead
            fill(255,255,255)
            rect(cell.x*16,cell.y*16,16,16)
        else: #alive
            alive += 1
            rand1 = random.randint(0,255)
            rand2 = random.randint(0,255)
            rand3 = random.randint(0,255)
            fill(rand1,rand2,rand3)
            #fill(0,0,0)
            rect(cell.x*16,cell.y*16,16,16)
        #update cell state
        cell.changeState()
    #print "finished draw"
    #print alive

run()