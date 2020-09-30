import pygame
from nodeClass import GREY

class Button:
    def __init__(self, color, x, y, width, height, fontSize, text = ''):
        self.color = color
        self.x = x
        self.y = y
        self.tempX = x
        self.tempY = y
        self.width = width
        self.height = height
        self.tempWidth = width
        self.tempHeight = height
        self.text = text
        self.isClicked = False
        self.fontSize = fontSize
        self.tempFont = fontSize

    def draw(self, win, outline = None):
        if outline: #Create button border
            pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':     #Create button text and center it
            font = pygame.font.SysFont('comicsans', self.fontSize)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def isOver(self, pos):  #Checks whether mouse is over the button
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False

    def clicked(self):  #If the button is clicked
        self.isClicked = True
        self.color = GREY

    def expand(self):   #Expand the button if the mouse hovers over it
        self.x = self.tempX - 2
        self.y = self.tempY - 2
        self.width  = self.tempWidth + 4
        self.height = self.tempHeight + 4
        self.fontSize = self.tempFont + 5

    def shrink(self):   #Shrink the button if the mouse hovers over it
        self.x = self.tempX
        self.y = self.tempY
        self.width  = self.tempWidth
        self.height = self.tempHeight
        self.fontSize = self.tempFont
