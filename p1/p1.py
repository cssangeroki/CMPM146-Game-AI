# Claudio Sangeroki, Conor Edgecumbe
# CMPM-146 P1 Dijkstra's Dungeon; 10/11/20
from p1_support import load_level, show_level, save_level_costs
from math import inf, sqrt
from heapq import heappop, heappush


def dijkstras_shortest_path(initial_position, destination, graph, adj):
    """ Searches for a minimal cost path through a graph using Dijkstra's algorithm.

    Args:
        initial_position: The initial cell from which the path extends.
        destination: The end location for the path.
        graph: A loaded level, containing walls, spaces, and waypoints.
        adj: An adjacency function returning cells adjacent to a given cell as well as their respective edge costs.

    Returns:
        If a path exits, return a list containing all cells from initial_position to destination.
        Otherwise, return None.

    """
    dist = {}
    prev = {}

    dist[initial_position] = 0
    prev[initial_position] = None

    priorityQueue = []
    # Initialize starting position
    heappush(priorityQueue, (dist[initial_position], initial_position))

    while priorityQueue:  # While queue is not empty

        currentCost, currentPos = heappop(
            priorityQueue)  # Extract shortest path node
        neighbors = adj(graph, currentPos)

        if currentPos == destination:   # Prints out path
            path = []
            currPath = destination
            while currPath is not None:
                path.insert(0, currPath)
                currPath = prev[currPath]
            return path

        for neighborPos, neighborCost in neighbors:

            alt = dist[currentPos] + neighborCost   # Cost

            if neighborPos not in dist or alt < dist[neighborPos]:
                dist[neighborPos] = alt
                prev[neighborPos] = currentPos
                heappush(priorityQueue, (alt, neighborPos))

    return []
    pass


def dijkstras_shortest_path_to_all(initial_position, graph, adj):
    """ Calculates the minimum cost to every reachable cell in a graph from the initial_position.

    Args:
        initial_position: The initial cell from which the path extends.
        graph: A loaded level, containing walls, spaces, and waypoints.
        adj: An adjacency function returning cells adjacent to a given cell as well as their respective edge costs.

    Returns:
        A dictionary, mapping destination cells to the cost of a path from the initial_position.
    """

    dist = {}
    prev = {}

    dist[initial_position] = 0
    prev[initial_position] = None

    priorityQueue = []
    heappush(priorityQueue, (dist[initial_position], initial_position))

    while priorityQueue:  # while queue is not empty

        currentCost, currentPos = heappop(
            priorityQueue)  # extract shortest path node
        neighbors = adj(graph, currentPos)

        # if currentPos == destination:
        #     path = []
        #     currPath = destination
        #     while currPath is not None:
        #         path.insert(0, currPath)
        #         currPath = prev[currPath]
        #     return path

        for neighborPos, neighborCost in neighbors:

            alt = dist[currentPos] + neighborCost

            if neighborPos not in dist or alt < dist[neighborPos]:
                dist[neighborPos] = alt
                prev[neighborPos] = currentPos
                heappush(priorityQueue, (alt, neighborPos))
    return dist


def navigation_edges(level, cell):
    spcs = level['spaces']
    wypts = level['waypoints']
    cX = cell[0]
    cY = cell[1]
    adj = []

    for x in range(cX - 1, cX + 2):
        for y in range(cY - 1, cY + 2):
            # if both coords are different -> diagonal
            if (x != cX and y != cY):
                if (x, y) in spcs:
                    w = 0.5 * (sqrt(2)) * \
                        (spcs[cX, cY]) + 0.5 * (sqrt(2)) * (spcs[x, y])
                    cellAdj = ((x, y), w)
                    adj.append(cellAdj)
            # if only one coord is different -> non-diagonal
            elif (x != cX or y != cY):
                if (x, y) in spcs:
                    w = 0.5 * (spcs[cX, cY]) + 0.5 * (spcs[x, y])
                    cellAdj = ((x, y), w)
                    adj.append(cellAdj)

    return adj


def test_route(filename, src_waypoint, dst_waypoint):
    """ Loads a level, searches for a path between the given waypoints, and displays the result.

    Args:
        filename: The name of the text file containing the level.
        src_waypoint: The character associated with the initial waypoint.
        dst_waypoint: The character associated with the destination waypoint.

    """

    # Load and display the level.
    level = load_level(filename)
    show_level(level)

    # Retrieve the source and destination coordinates from the level.
    src = level['waypoints'][src_waypoint]
    dst = level['waypoints'][dst_waypoint]

    # Search for and display the path from src to dst.
    path = dijkstras_shortest_path(src, dst, level, navigation_edges)
    if path:
        show_level(level, path)
    else:
        print("No path possible!")


def cost_to_all_cells(filename, src_waypoint, output_filename):
    """ Loads a level, calculates the cost to all reachable cells from 
    src_waypoint, then saves the result in a csv file with name output_filename.

    Args:
        filename: The name of the text file containing the level.
        src_waypoint: The character associated with the initial waypoint.
        output_filename: The filename for the output csv file.

    """

    # Load and display the level.
    level = load_level(filename)
    show_level(level)

    # Retrieve the source coordinates from the level.
    src = level['waypoints'][src_waypoint]

    # Calculate the cost to all reachable cells from src and save to a csv file.
    costs_to_all_cells = dijkstras_shortest_path_to_all(
        src, level, navigation_edges)
    save_level_costs(level, costs_to_all_cells, output_filename)


if __name__ == '__main__':
    filename, src_waypoint, dst_waypoint = 'my_maze.txt', 'a', 'd'

    # Use this function call to find the route between two waypoints.
    test_route(filename, src_waypoint, dst_waypoint)

    # Use this function to calculate the cost to all reachable cells from an origin point.
    cost_to_all_cells(filename, src_waypoint, 'my_maze_costs.csv')
