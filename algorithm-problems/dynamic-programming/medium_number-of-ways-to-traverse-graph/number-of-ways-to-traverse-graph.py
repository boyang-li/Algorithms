# Notes:
# We can use Dynamic Programming to solve this problem in the optimal way.
# Realise the fact that if we are at any border cell(top or left), the number
# of ways to traverse to that cell is only one, because by setup we only go
# right or go down in the matrix.
#
# For any other cell in the matrix, the number of ways to traverse to that cell
# is the sum of the ways to traverse to the neighboring cells in the up and left
# directions.
#
# We could traverse the matrix in zig-zag pattern starting form the top-left
# cell, and gradualy fill all cells up by calculating the number of ways to
# traverse to it by summing up the results of its top and left neighbors.
#
# Complexity:
# O(n * m) time | O(n * m) space - where n is the height and m is the width.
def numberOfWaysToTraverseGraph(width, height):
    numberOfWays = [[0 for _ in range(width + 1)] for _ in range(height + 1)]

    for widthIdx in range(1, width + 1):
        for heightIdx in range(1, height + 1):
            if widthIdx == 1 or heightIdx == 1:
                numberOfWays[heightIdx][widthIdx] = 1
            else:
                waysLeft = numberOfWays[heightIdx][widthIdx - 1]
                waysUp = numberOfWays[heightIdx - 1][widthIdx]
                numberOfWays[heightIdx][widthIdx] = waysLeft + waysUp

    return numberOfWays[height][width]
