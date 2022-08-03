# Notes:
# We can solve this problem using the iterative approach. We use an auxiliary
# matrix with the same dimensions to track the visited elements throughout the
# main iteration and the neightbor explorations. We keep mutate island tiles to
# land tiles by flippint the 1's to 0's as we traverse the matrix.
#
# Note that an island must satisfy the following conditions:
# 1. cannot conect to the border, that is not horizontally or vertically
# adjacent to a land tile on border.
# 2. the land tiles of the island must be either horizontally or vertically
# adjacent to each others, diagonally adjacent tiles are not considered.
#
# Complexity:
# O(n * m) time | O(n * m) space - where m and n are the width and height of the
# input matrix.
def removeIslands(matrix):
    # create an auxiliary matrix to keep track of visited nodes
    visited = [[False for value in row] for row in matrix]
    # the main loop to iterate through the matrix.
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            # if element is visited, skip it
            if visited[i][j]:
                continue
            # try to explore from the element to detect and remove potential
            # island tiles in place.
            traverseNode(i, j, matrix, visited)
    return matrix

def traverseNode(i, j, matrix, visited):
    connectToLand = False
    nodesToRemove = []
    nodesToExplore = [[i, j]]
    while len(nodesToExplore) > 0:
        currentNode = nodesToExplore.pop()
        i = currentNode[0]
        j = currentNode[1]
        # check whether the tile is visited.
        if visited[i][j]:
            continue
        visited[i][j] = True
        # check whether the tile is land
        if matrix[i][j] == 0:
            continue

        # check whether the tile is on border
        if i==0 or i==len(matrix) - 1 or j==0 or j == len(matrix[0]) - 1:
            # the tile is land and it is on border, which means all the tiles
            # connected to it in this iteration can not form an island, hence,
            # there are no land tiles to remove! But, we still need to update
            # the visited matrix, so do not break out the loop.
            connectToLand = True
        elif not connectToLand:
            nodesToRemove.append([i, j])

        unvisitedNeighbors = getUnvisitedNeighbors(i, j, matrix, visited)
        for neighbor in unvisitedNeighbors:
            nodesToExplore.append(neighbor)
    # convert land tiles to water tiles.
    if not connectToLand:
        for node in nodesToRemove:
            i = node[0]
            j = node[1]
            matrix[i][j] = 0

# explores the directly adjacent tiles to get the unvisited neighbors.
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
