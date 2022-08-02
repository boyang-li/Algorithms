# Notes:
# We use recursion to solve this problem. We will also need auxiliary data
# structure to store states of visited nodes, and the states are: 'unvisited',
# 'inStatck', and 'done', which are represented in color integers (white - 0,
# blue - 1, red - 2).
#
# We run Depth First Search on the graph, and update the state of nodes as we
# traverse. We continue to traverse the graph until we have found a cycle--
# visiting a node with the blue state, which means it is visited before and
# we have a "back edge".
#
# Complexity:
# O(v + e) time | O(v) space - where v is the number of vertices, and e is the
# number of edges.
WHITE, BLUE, RED = 0, 1, 2

def cycleInGraph(edges):
    numOfNodes = len(edges)
    colors = [WHITE for _ in range(numOfNodes)]

    for node in range(numOfNodes):
        if colors[node] != WHITE:
            continue

        containsCycle = traverseAndColorNodes(node, edges, colors)
        if containsCycle:
            return True

    return False

def traverseAndColorNodes(node, edges, colors):
    colors[node] = BLUE

    neighbors = edges[node]
    for neighbor in neighbors:
        neighborColor = colors[neighbor]

        if neighborColor == BLUE:
            return True

        if neighborColor == RED:
            continue

        containsCycle = traverseAndColorNodes(neighbor, edges, colors)
        if containsCycle:
            return True

    colors[node] = RED
    return False
