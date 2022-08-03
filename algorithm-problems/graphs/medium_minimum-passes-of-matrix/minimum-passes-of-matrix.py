# Notes:
# We can solve this problem using the iterative approach. First, we use an auxiliary
# matrix with the same dimensions to get the positions of the positive elements.
# Note that the algorithm work by continuously traversing the updated positions
# of positive elements, explore and convert their direct adjacent neighbors.
#
# The catch is that once the negative neighbor of a positive element is flipped
# to positive, we can immediate add that neighbor to the positive elements
# to be traversed in the next pass, because it can further convert its negative
# neighbors now.
#
# We keep mutate the elements of the matrix in place until there is no more
# newly converted positive elements to traverse, adn return the count of
# minimum passes.
#
# Complexity:
# Realise the face that we are only visiting an element in the matrix once,
# because once an element if popped off the queue, it is never added back.
# O(n * m) time | O(n * m) space - where m is the width of the matrix and n is
# the height of the matrix.
def minimumPassesOfMatrix(matrix):
    passes = convertNegatives(matrix)
    # note that we need to minus 1 from the minimum passes counter, because the
    # last iteration does NOT convert any negative elements. And if
    return passes - 1 if not containsNegative(matrix) else -1

def convertNegatives(matrix):
    # we use a queue data structure and populate it with the positions of the
    # positive elements in the matrix.
    nextPassQueue = getAllPositivePositions(matrix)

    # a counter for the minimum passes of matrix
    passes = 0

    # so long as the queue is not empty, continue the loop.
    while len(nextPassQueue) > 0:
        # Realise the fact that the negative elements in the current pass will
        # be converted to positive elements, and they can further convert the
        # negative neighbors in the next pass. So, we create an empty queue to
        # hold the POSITIVE elements for the next pass.
        currentPassQueue = nextPassQueue
        nextPassQueue = []

        # so long as the current queue is not empty, continue the traversal.
        while len(currentPassQueue) > 0:
            # pop an element in FIFO order
            currRow, currCol = currentPassQueue.pop(0)
            # get the adjacent neighbors, convert the negative elements and
            # push the newly converted ones to the queue.
            adjPositions = getAdjPositions(currRow, currCol, matrix)
            for pos in adjPositions:
                i, j = pos
                value = matrix[i][j]
                if value < 0:
                    matrix[i][j] *= -1
                    nextPassQueue.append([i, j])
        # update the minimum passes counter
        passes += 1
    return passes

# This helper function returns all the positions of all the positive elements
# in the input matrix.
# O(n * m) time | O(n * m) space
def getAllPositivePositions(matrix):
    # a list to hold the output in coordinates i.e.[[i, j], ...]
    positivePositions = []

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            value = matrix[i][j]
            if value > 0:
                positivePositions.append([i, j])

    return positivePositions

# This helper function returns the positions of the directly adjacent neighbors
# of the given position.
def getAdjPositions(i, j, matrix):
    adjPositions = []
    if i > 0: adjPositions.append([i - 1, j])
    if i < len(matrix) - 1: adjPositions.append([i + 1, j])
    if j > 0: adjPositions.append([i, j - 1])
    if j < len(matrix[0]) - 1: adjPositions.append([i, j + 1])
    return adjPositions

# This helper function checks whether the matrix contains any negative element.
def containsNegative(matrix):
    for row in matrix:
        for v in row:
            if v < 0:
                return True
    return False
