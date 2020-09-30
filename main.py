from drawGrid import *


# HELPER FUNCTIONS
def getClickedPos(position, rows, width):
    gap = width // rows
    y, x = position

    row = y // gap
    col = x // gap

    return row, col

def resetAllButtons():   #reset all button original state
    for button in algorithmButtons:
        button.isClicked = False
        button.color = WHITE

def checkButtonHover(position): #Check if mouse is over the button and either highlights it or expand it
    for button in allButtons:
        if button.isOver(position):
            if button in (startButton, resetButton):
                button.expand()
            else:
                button.color = GREY
        else:
            if not button.isClicked and button not in (startButton, resetButton):
                button.color = WHITE
            else:
                button.shrink()

def checkButtonClicked(position, prevButton):   #Check if any of the algorithm buttons are clicked
    for button in algorithmButtons:
        if button.isOver(position):
            button.clicked()
            resetPrevButton(prevButton, button)
            prevButton = button

    return prevButton

def resetPrevButton(prevButton, currentButton): #Reset the previous clicked button when a new button is pressed
    if prevButton and prevButton != currentButton:
        prevButton.isClicked = False
        prevButton.color = WHITE


# RUN GAME
def main(win, width):
    ROWS = 35   #Define how many rows for the grid
    grid = makeGrid(ROWS, width) #Create the grid array

    startNode = None
    endNode = None
    selectedButton = None
    run = True  #If main loop is running or not
    started = False     #If the start button is pressed or not

    #GAME LOOP
    while run:
        draw(win, grid, ROWS, width)    #Draw grid on every loop
        for event in pygame.event.get():    #At beginning of each of while loop, loop through all events that have happened & check what they are
            if event.type == pygame.QUIT:  #Check if user pressed x button at top right, stop the game
                run = False

            mousePos = pygame.mouse.get_pos()   #Get position of mouse on screen

            checkButtonHover(mousePos)  #Check whether the mouse hovers over a button

            if pygame.mouse.get_pressed()[0]:   #Check if left mouse button is pressed
                if started == False: #Only allow for the algorithm and start buttons to be pressed if the algorithm has not been run yet
                    selectedButton = checkButtonClicked(mousePos, selectedButton)

                    row, col = getClickedPos(mousePos, ROWS, width)     #Get which Node the mouse clicked on
                    if mousePos[0] < width and mousePos[1] < width:
                        node = grid[row][col]
                        if not startNode and node != endNode:   #Check if start Node have been clicked
                            startNode = node
                            startNode.makeStart()

                        elif not endNode and node != startNode:   #Check if end Node have been clicked
                            endNode = node
                            endNode.makeEnd()

                        elif node != startNode and node != endNode: #If start and end Node have been created, any clicks after will be barriers
                            node.makeBarrier()

                    if startButton.isOver(mousePos) and startNode and endNode and selectedButton:    #Check if start button is pressed
                        for row in grid:    #Update neighboring Nodes for each Node
                            for node in row:
                                node.updateNeighbors(grid)

                        algorithm = selectedButton.text
                        if algorithm == 'Breadth-first Search':
                            solveBFS(lambda: draw(win, grid, ROWS, width), startNode, endNode)
                        if algorithm == 'Depth-first Search':
                            solveDFS(lambda: draw(win, grid, ROWS, width), startNode, endNode)
                        if algorithm == 'A* Search':
                            solveAStar(lambda: draw(win, grid, ROWS, width), startNode, endNode)
                        if algorithm == 'Dijkstra\'s Algorithm':
                            solveDijkstra(lambda: draw(win, grid, ROWS, width), startNode, endNode)

                        started = True  #Set to true because the algorithm ran

                if resetButton.isOver(mousePos):    #Check if reset button is pressed
                    startNode = None
                    endNode = None
                    selectedButton = None
                    started = False
                    resetAllButtons()
                    grid = makeGrid(ROWS, width) #Clear the entire grid


            elif pygame.mouse.get_pressed()[2]:  #Check if right mouse button is pressed
                row, col = getClickedPos(mousePos, ROWS, width)     #Get which Node the mouse clicked on
                if mousePos[0] < width and mousePos[1] < width and started == False:
                    node = grid[row][col]
                    node.reset()    #Clear Node back to WHITE
                    if node == startNode:   #Reset startNode
                        startNode = None
                    elif node == endNode:   #Reset endNode
                        endNode = None

    pygame.quit()   #Exit pygame window

main(WIN, WIDTH)
