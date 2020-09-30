from pathAlgorithms import *
import pygame
import math
from buttonClass import *

WIDTH = 700
appHEIGHT = WIDTH + 200
WIN = pygame.display.set_mode((WIDTH,appHEIGHT)) #Initialize display window/screen
pygame.display.set_caption("My Pathfinding Visualizer") #Set display window title
pygame.font.init()  #Initialize fonts for Button class

#Buttons Initialization
heightGap = 40
widthGap = 50
BFSbutton = Button(WHITE, 30, WIDTH + 40, 200, 40, 30, 'Breadth-first Search')
DFSbutton = Button(WHITE, 30, BFSbutton.y + BFSbutton.height + heightGap, 200, 40, 30, 'Depth-first Search')
aStarButton = Button(WHITE, BFSbutton.x + BFSbutton.width + widthGap, BFSbutton.y, 200, 40, 30, 'A* Search')
dijkstraButton = Button(WHITE, DFSbutton.x + DFSbutton.width + widthGap, DFSbutton.y, 200, 40, 30, 'Dijkstra\'s Algorithm')
startButton = Button(GREEN, aStarButton.x + aStarButton.width + 75, WIDTH + 30, 100, 60, 40, 'Start')
resetButton = Button(RED, startButton.x + 10, startButton.y + startButton.height + 30, 80, 50, 30, 'Reset')

#Holds all the algorithm buttons
algorithmButtons = [BFSbutton, DFSbutton, aStarButton, dijkstraButton]

#Holds all the Buttons
allButtons = algorithmButtons + [startButton, resetButton]


#MAKE GAME GRID
def makeGrid(rows, width):  #width = entire width of grid, rows = # of rows
    grid = []
    gap = width // rows     #gap = width of each Node (// - integer division)
    for i in range(rows):   #Creating a 2D list - [[Node], [Node], [Node],
        grid.append([])                         #  [Node], [Node], [Node]]
        for j in range(rows):
            node = Node(i, j, gap, rows)
            grid[i].append(node)    #In grid row i, add Node to grid

    return grid

def drawGrid(win, rows, width):     #draw grid lines, not Nodes
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))     #Draw horizontal lines for each rows
        pygame.draw.line(win, GREY, (i * gap, 0), (i * gap, width)) #Draw vertical lines for each cols

    pygame.draw.line(win, GREY, (0, WIDTH), (WIDTH, WIDTH)) # Draw the last horizontal line

def draw(win, grid, rows, width):
    win.fill(WHITE)  #Fill entire screen with one color (do it at beginning of every frame)

    #Draw last horizontal line to separate the game grid and the buttons
    pygame.draw.line(win, GREY, (aStarButton.x + aStarButton.width + 30, WIDTH), (aStarButton.x + aStarButton.width + 30, appHEIGHT))

    for row in grid:
        for node in row:
            node.draw(win)

    #Draw Buttons
    DFSbutton.draw(win, BLACK)
    BFSbutton.draw(win, BLACK)
    aStarButton.draw(win, BLACK)
    dijkstraButton.draw(win, BLACK)
    startButton.draw(win, BLACK)
    resetButton.draw(win, BLACK)

    drawGrid(win, rows, width)   #Draw grid lines on top of filled screen
    pygame.display.update()     #Take whatever we just drawn and update that on display
