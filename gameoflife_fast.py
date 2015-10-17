from pyprocessing import *
import random

cells = []
debug = False
global color1
color1 = 0
global backward
backward = False

class Cell():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.state = 0#random.randint(0,3) #dead by default
        self.adjacent = []
        self.aliveNeighbors = 0

    def getAdjacent(self):
        self.aliveNeighbors = 0
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
                elif self.y == cell.y:
                    midLeft = cell
                elif self.y+1 == cell.y:
                    lowLeft = cell
            elif self.x == cell.x:
                if self.y-1 == cell.y:
                    topMid = cell
                elif self.y+1 == cell.y:
                    lowMid = cell
            elif self.x+1 == cell.x:
                if self.y-1 == cell.y:
                    topRight = cell
                elif self.y == cell.y:
                    midRight = cell
                elif self.y+1 == cell.y:
                    lowRight = cell
        self.adjacent = [topLeft,midLeft,lowLeft,topMid,lowMid,topRight,midRight,lowRight]

    def changeState(self):
        adj_alive = 0
        self.getAdjacent()
        for item in self.adjacent:
            if item != None:
                if item.state == 1:
                    adj_alive += 1
        if self.state == 1: #alive
            #underpopulation
            if adj_alive < 2:
                self.state = 0
            #overcrowding
            elif adj_alive > 3:
                self.state = 0
            #alive...for now
            else:
                self.state = 1 #unnecessary line
        else: #dead
            #reproduction
            if adj_alive == 3:
                self.state = 1

def change_states():
    for cell in cells:
        cell.getAdjacent()
        for item in cell.adjacent:
            if item != None:
                if item.state == 1:
                    cell.aliveNeighbors += 1
    for cell in cells:
        if cell.state == 1:
            #underpopulation
            if cell.aliveNeighbors < 2:
                cell.state = 0
            #overcrowding
            elif cell.aliveNeighbors > 3:
                cell.state = 0
            #alive...for now
            else:
                cell.state = 1 #unnecessary line
        else: #dead
            #reproduction
            if cell.aliveNeighbors == 3:
                cell.state = 1


def setup():
    #print "ran setup"
    size(660,500,fullscreen=False)
    noStroke()
    alive = 0
    for x in range(0,33):
        for y in range(0,25):
            #randState = random.randint(0,1)
            #newCell = Cell(x,y,randState)
            newCell = Cell(x,y)

            #SIMKIN GLIDER GUN
            if y == 2 or y == 3:
                if x == 2 or x == 3 or x == 9 or x == 10:
                    newCell.state = 1
            elif y == 5 or y == 6:
                if x == 6 or x == 7:
                    newCell.state = 1
            elif y == 11:
                if x == 24 or x == 25 or x == 27 or x == 28:
                    newCell.state = 1
            elif y == 12:
                if x == 23 or x == 29:
                    newCell.state = 1
            elif y == 13:
                if x == 23 or x == 30 or x == 33 or x == 34:
                    newCell.state = 1
            elif y == 14:
                if x == 23 or x == 24 or x == 25 or x == 29 or x == 33 or x == 34:
                    newCell.state = 1
            elif y == 15:
                if x == 28:
                    newCell.state = 1
            elif y == 19:
                if x == 22 or x == 23:
                    newCell.state = 1
            elif y == 20:
                if x == 22:
                    newCell.state = 1
            elif y == 21:
                if x == 23 or x == 24 or x == 25:
                    newCell.state = 1
            elif y == 22:
                if x == 25:
                    newCell.state = 1


            '''
            #GLIDER
            if y == 2 and x == 3:
                newCell.state = 1
            if y == 3 and x == 4:
                newCell.state = 1
            if y == 4:
                if x == 2 or x == 3 or x == 4:
                    newCell.state = 1
            '''
            '''
            #CLOCK
            if y == 23:
                if x == 25:
                    newCell.state = 1
                    alive += 1
            elif y == 24:
                if x == 23:
                    newCell.state = 1
                    alive += 1
                elif x == 25:
                    newCell.state = 1
                    alive += 1
            elif y == 25:
                if x == 24:
                    newCell.state = 1
                    alive += 1
                elif x == 26:
                    newCell.state = 1
                    alive += 1
            elif y == 26:
                if x == 24:
                    newCell.state = 1
                    alive += 1

            #Diehard
            if y == 14:
                if x == 6:
                    newCell.state = 1
            elif y == 15:
                if x == 10:
                    newCell.state = 1
                if x == 11:
                    newCell.state = 1
            elif y == 16:
                if x == 1:
                    newCell.state = 1
                if x == 5:
                    newCell.state = 1
                if x == 6:
                    newCell.state = 1
                if x == 7:
                    newCell.state = 1

            #Diehard
            if y == 17:
                if x == 7:
                    newCell.state = 1
            elif y == 18:
                if x == 15:
                    newCell.state = 1
                if x == 16:
                    newCell.state = 1
            elif y == 19:
                if x == 6:
                    newCell.state = 1
                if x == 10:
                    newCell.state = 1
                if x == 11:
                    newCell.state = 1
                if x == 12:
                    newCell.state = 1

            #???
            if y == 34:
                if x == 35:
                    newCell.state = 1
                if x == 34:
                    newCell.state = 1
            if y == 35:
                if x == 34:
                    newCell.state = 1
            if y == 37:
                if x == 34:
                    newCell.state = 1
                if x == 35:
                    newCell.state = 1
                if x == 36:
                    newCell.state = 1
            '''
            cells.append(newCell)
    #print alive

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
    '''

def draw():
    #print "ran draw"
    if debug == True: #maintain initial state for debugging
        #fill(200,50)
        fill(255)
        rect(0,0,660,500)
        fill(0)
        draw_alive = 0
        for cell in cells:
            if cell.state == 0: #dead
                fill(255,255,255)
                rect(cell.x*20,cell.y*20,20,20)
            else: #alive
                draw_alive += 1
                #rand1 = random.randint(0,255)
                #rand2 = 80#random.randint(0,255)
                #rand3 = 150#random.randint(0,255)
                global color1
                global backward
                if color1 == 255:
                    backward = True
                if color1 == 0:
                    backward = False
                if backward == False:
                    color1 = color1 + 1
                else:
                    color1 = color1 - 1
                fill(240,color1,50)
                #fill(rand1,rand2,rand3)
                #fill(0,0,0)
                rect(cell.x*20,cell.y*20,20,20)
        #print alive
    else: #game of life
        #fill(200,50)
        fill(255)
        rect(0,0,330,250)
        fill(0)
        draw_alive = 0
        for cell in cells:
            if cell.state == 0: #dead
                fill(255,255,255)
                rect(cell.x*20,cell.y*20,20,20)
            elif cell.state == 1: #alive
                draw_alive += 1
                rand1 = 40#random.randint(0,55)
                #rand2 = random.randint(0,255)#80
                rand3 = 150#random.randint(0,255)
                global color1
                global backward
                if color1 == 255:
                    backward = True
                if color1 == 0:
                    backward = False
                if backward == False:
                    color1 = color1 + 1
                else:
                    color1 = color1 - 1
                fill(rand1,color1,rand3)
                #fill(0,0,0)
                rect(cell.x*20,cell.y*20,20,20)
        #print "finished draw"
        change_states()
        #for cell in cells:
        #    cell.changeState()
        #print draw_alive

run()