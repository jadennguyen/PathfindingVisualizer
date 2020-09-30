from nodeClass import *
from queue import PriorityQueue, Queue
from collections import deque

def Heuristic(p1, p2):  #p1, p2 are point 1 & point 2
    x1, y1 = p1     #p1, p2 are tuples
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)

def reconstructPath(currentNode, draw):
    startToEnd = []
    while currentNode.parent != None:   #Reorder the nodes from start to end instead of end to start
        currentNode = currentNode.parent
        startToEnd.append(currentNode)

    while startToEnd:
        node = startToEnd.pop()
        node.makePath()
        draw()


def solveAStar(draw, startNode, endNode):
    count = 0
    uncheckedNodes = PriorityQueue()
    uncheckedNodes.put((0, count, startNode))
    startNode.updategScore(0)
    startNode.updatefScore(Heuristic(startNode.getPos(), endNode.getPos()))
    startNode.setVisited()

    while not uncheckedNodes.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        currentNode = uncheckedNodes.get()[2]

        if currentNode == endNode:
            reconstructPath(currentNode, draw)
            endNode.makeEnd()
            return True

        for neighborNode in currentNode.neighbors:

            temp_gScore = currentNode.gScore + 1

            if temp_gScore < neighborNode.gScore:
                neighborNode.updateParent(currentNode)
                neighborNode.updategScore(temp_gScore)
                new_fScore = temp_gScore + Heuristic(neighborNode.getPos(), endNode.getPos())
                neighborNode.updatefScore(new_fScore)
                if not neighborNode.visited:
                    count += 1
                    neighborNode.setVisited()
                    uncheckedNodes.put((neighborNode.fScore, count, neighborNode))

        draw()

        if currentNode != startNode:
            currentNode.makeClosed() #If Node we're looking at is not the startNode, close it off

    return False


def solveDijkstra(draw, startNode, endNode):
    count = 0
    uncheckedNodes = PriorityQueue()
    uncheckedNodes.put((0, count, startNode))
    startNode.updategScore(0)
    startNode.updatefScore(Heuristic(startNode.getPos(), endNode.getPos()))

    while not uncheckedNodes.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        currentNode = uncheckedNodes.get()[2]
        currentNode.setVisited()

        if currentNode == endNode:
            reconstructPath(currentNode, draw)
            endNode.makeEnd()
            return True

        for neighborNode in currentNode.neighbors:

            temp_gScore = currentNode.gScore + 1

            if temp_gScore < neighborNode.gScore:
                neighborNode.updateParent(currentNode)
                neighborNode.updategScore(temp_gScore)
                new_fScore = temp_gScore
                neighborNode.updatefScore(new_fScore)
                if not neighborNode.visited:
                    count += 1
                    uncheckedNodes.put((neighborNode.fScore, count, neighborNode))

        draw()

        if currentNode != startNode:
            currentNode.makeClosed() #If Node we're looking at is not the startNode, close it off

    return False


def solveBFS(draw, startNode, endNode):
    nodeToTest = Queue()
    nodeToTest.put(startNode)
    startNode.setVisited()

    while not nodeToTest.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        currentNode = nodeToTest.get()

        if currentNode == endNode:
            reconstructPath(currentNode, draw)
            endNode.makeEnd()
            return True

        for neighborNode in currentNode.neighbors:
            if not neighborNode.visited:
                neighborNode.setVisited()
                neighborNode.updateParent(currentNode)
                nodeToTest.put(neighborNode)

        draw()

        if currentNode != startNode:
            currentNode.makeClosed()

    return False


def solveDFS(draw, startNode, endNode):
    nodeToTest = deque()
    nodeToTest.append(startNode)

    while nodeToTest:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        currentNode = nodeToTest.pop()
        currentNode.setVisited()

        if currentNode == endNode:
            reconstructPath(currentNode, draw)
            endNode.makeEnd()
            return True

        for neighborNode in currentNode.neighbors:
            if not neighborNode.visited:
                #neighborNode.setVisited()
                neighborNode.updateParent(currentNode)
                nodeToTest.append(neighborNode)

        draw()

        if currentNode != startNode:
            currentNode.makeClosed()

    return False
