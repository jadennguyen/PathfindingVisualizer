import pygame
import os.path

#Get Images (20 x 20)
filepath = os.path.dirname(__file__)
image_path = os.path.join(filepath, 'Images')
targetImg = pygame.image.load(os.path.join(image_path, "targetResized.png"))
starImg = pygame.image.load(os.path.join(image_path, "starIconResized.png"))
rightArrowImg = pygame.image.load(os.path.join(image_path, "rightArrowResized.png"))

#COLORS
RED = (255, 0, 0)
GREEN = (0, 255, 0)
UCLAblue = (50, 132, 191)
UCLAgold = (255, 209, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0 ,0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

class Node:
    def __init__(self, row, col, width, totalRows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.visited = False
        self.gScore = float("inf")
        self.fScore = float("inf")
        self.parent = None
        self.neighbors = []
        self.width = width
        self.totalRows = totalRows
        self.img = None

    def getPos(self):
        return self.row, self.col   #(row, col)

    def isBarrier(self):
        return self.color == BLACK

    def reset(self):
        self.color = WHITE
        self.img = None

    def makeClosed(self):
        self.color = TURQUOISE

    def makeBarrier(self):
        self.color = BLACK

    def makeStart(self):
        self.img = rightArrowImg

    def makeEnd(self):
        self.color = RED
        #self.img = pygame.transform.scale(targetImg, (self.width , self.width))
        self.img = targetImg

    def makePath(self):
        self.color = UCLAgold

    def draw(self, win):    #Draw square Node
        if self.img != None:
            win.blit(self.img, (self.x, self.y))
        else:
            pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def updateNeighbors(self,grid):    #Get neighboring Node
        self.neighbors = []
        if self.row > 0 and not grid[self.row - 1][self.col].isBarrier(): #LEFT
            self.neighbors.append(grid[self.row - 1][self.col])

        if self.col < self.totalRows - 1 and not grid[self.row][self.col + 1].isBarrier(): #DOWN
            self.neighbors.append(grid[self.row][self.col + 1])

        if self.row < self.totalRows - 1 and not grid[self.row + 1][self.col].isBarrier(): #RIGHT
            self.neighbors.append(grid[self.row + 1][self.col])

        if self.col > 0 and not grid[self.row][self.col - 1].isBarrier(): #UP
            self.neighbors.append(grid[self.row][self.col - 1])

    def updateParent(self, parentNode):
        self.parent = parentNode

    def updategScore(self, gScore):
        self.gScore = gScore

    def updatefScore(self, fScore):
        self.fScore = fScore

    def setVisited(self):
        self.visited = True

    def __lt__(self, other):   #Override equality operator
        return False
