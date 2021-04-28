
from math import sqrt
from heapq import heappop, heappush


def find_path(source_point, destination_point, mesh):
    """
    Searches for a path from source_point to destination_point through the mesh

    Args:
        source_point: starting point of the pathfinder
        destination_point: the ultimate goal the pathfinder must reach
        mesh: pathway constraints the path adheres to

    Returns:

        A path (list of points) from source_point to destination_point if exists
        A list of boxes explored by the algorithm
    """

    path = []
    boxes = {}

    sourceBox = None
    destBox = None

    # print(mesh)

    for box in mesh['boxes']:
        if box not in boxes and inBox(box, source_point):
            sourceBox = box
            # print(sourceBox)
        if box not in boxes and inBox(box, destination_point):
            destBox = box
            # print(destBox)

    if (sourceBox is None) or (destBox is None):
        print("No Path!")
        return [], []

    dist = {}
    prev = {}
    boxCoords = {}

    dist[sourceBox] = 0
    prev[sourceBox] = None
    boxCoords[sourceBox] = source_point

    priorityQueue = []
    heappush(priorityQueue, (dist[sourceBox], sourceBox))

    adj = mesh["adj"]

    while priorityQueue:

        currentCost, currentPos = heappop(priorityQueue)
        #neighbors = adj(graph, currentPos)

        # if currentPos == destination:
        #     path = []
        #     currPath = destination
        #     while currPath is not None:
        #         path.insert(0, currPath)
        #         currPath = prev[currPath]
        #     return path

        if currentPos == destBox:
            path = [boxCoords[currentPos], destination_point]

            backBox = prev[currentPos]
            backCoord = boxCoords[currentPos]

            while backBox is not None:
                path.insert(0, [boxCoords[backBox], backCoord])
                backBox = prev[backBox]
                backCoord = boxCoords[backBox]
                print(backCoord)

            return path, boxes.keys()

        # for neighborPos, neighborCost in neighbors:

        #     alt = dist[currentPos] + neighborCost

        #     if neighborPos not in dist or alt < dist[neighborPos]:
        #         dist[neighborPos] = alt
        #         prev[neighborPos] = currentPos
        #         heappush(priorityQueue, (alt, neighborPos))

        for neighbor in adj[currentPos]:

            boxes[neighbor] = currentPos

            xRange = [max(currentPos[0], neighbor[0]),
                      min(currentPos[1], neighbor[1])]
            yRange = [max(currentPos[2], neighbor[2]),
                      min(currentPos[3], neighbor[3])]

            firstCost = euclideanDistance(
                (xRange[0], yRange[0]), boxCoords[currentPos])
            secondCost = euclideanDistance(
                (xRange[1], yRange[1]), boxCoords[currentPos])

            if firstCost <= secondCost:
                finalCost = firstCost
                finalPoint = (xRange[0], yRange[0])
            else:
                finalCost = secondCost
                finalPoint = (xRange[1], yRange[1])

            alt = currentCost + finalCost
            if neighbor not in dist or alt < dist[neighbor]:
                dist[neighbor] = alt
                prev[neighbor] = currentPos
                boxCoords[neighbor] = finalPoint
                heappush(priorityQueue, (alt, neighbor))
    return None


def inBox(box, point):
    x1, x2, y1, y2 = box
    p1, p2 = point

    xInside = False
    yInside = False

    if x1 <= p1 and x2 >= p1:
        xInside = True
    if y1 <= p2 and y2 >= p2:
        yInside = True

    return xInside and yInside


def euclideanDistance(p1, p2):
    return sqrt(((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2))
