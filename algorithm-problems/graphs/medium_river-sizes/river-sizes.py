# Notes:
# We can solve this problem using the iterative approach. We use an auxiliary
# matrix of the same dimension to track the visited elements throughout the
# main iteration and the neightbor explorations. We keep track of the river
# sizes as we iterate through the matrix.
#
# Complexity:
# O(n * m) time | O(n * m) space - where m and n are the width and height of the
# input matrix.

# This is the main function of the algorithm.
def riverSizes(matrix):
    sizes = []
    # create an auxiliary matrix to keep track of visited nodes
    visited = [[False for v in row] for row in matrix]
    # the main loop to iterate through the matrix.
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            # if element is visited, skip it
            if visited[i][j]:
                continue
            # try to explore from the element to get size of potential river.
            traverseNode(i, j, matrix, visited, sizes)
    return sizes

# This function explores from a given node to get the size of a potential river.
def traverseNode(i, j, matrix, visited, sizes):
    currentRiverSize = 0
    # a list to hold nodes to explore, initialized with the current node.
    nodesToExplore = [[i, j]]
    # keep iterating the node list until it is empty.
    while len(nodesToExplore):
        currentNode = nodesToExplore.pop()
        i = currentNode[0]
        j = currentNode[1]
        # important! this check is necessary to make sure we do not have
        # repeated visits.
        if visited[i][j]:
            continue
        visited[i][j] = True
        # if we hit a land tile, skip it.
        if matrix[i][j] == 0:
            continue

        currentRiverSize += 1
        # for each nodes, we get the unvisited nodes and push them into the
        # list.
        unvisitedNeighbors = getUnvisitedNeighbors(i, j, matrix, visited)
        for neighbor in unvisitedNeighbors:
            nodesToExplore.append(neighbor)
    # add the river size to the output.
    if currentRiverSize > 0:
        sizes.append(currentRiverSize)

# This function
def getUnvisitedNeighbors(i, j, matrix, visited):
    unvisitedNeighbors = []
    # check whether we can visit top neighbor.
    if i > 0 and not visited[i - 1][j]:
        unvisitedNeighbors.append([i - 1, j])
    # check whether we can visit bottom neighbor.
    if i < len(matrix) - 1 and not visited[i + 1][j]:
        unvisitedNeighbors.append([i + 1, j])
    # check whether we can visit left neighbor.
    if j > 0 and not visited[i][j - 1]:
        unvisitedNeighbors.append([i, j - 1])
    # check whether we can visit right neighbor.
    if j < len(matrix[0]) - 1 and not visited[i][j + 1]:
        unvisitedNeighbors.append([i, j + 1])
    return unvisitedNeighbors
