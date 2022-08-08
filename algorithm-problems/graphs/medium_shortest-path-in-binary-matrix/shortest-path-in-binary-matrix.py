# LeetCode 1091. Shortest Path in Binary Matrix
from collections import deque

class Solution:
    # Approach 1: Breadth-first Search (BFS), Overwriting Input
    # Complexity:
    # O(n) time | O(n) space - n is the number of cells in the matrix.
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        maxRow = len(grid) - 1
        maxCol = len(grid[0]) - 1
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        # helper to find the neighbors of a given cell.
        def getNeighbors(row, col):
            for rowOffset, colOffset in directions:
                newRow = row + rowOffset
                newCol = col - colOffset
                # check if the new cell is in bounds
                if not (0 <= newRow <= maxRow and 0 <= newCol <= maxCol):
                    continue
                # check if it is a valid cell to go to
                if grid[newRow][newCol] != 0:
                    continue
                yield (newRow, newCol)

        if grid[0][0] != 0 or grid[maxRow][maxCol] != 0:
            return -1

        # The BFS search algo
        queue = deque()
        queue.append((0, 0))
        grid[0][0] = 1

        while queue:
            row, col = queue.popleft()
            distance = grid[row][col]
            if (row, col) == (maxRow, maxCol):
                return distance
            for neighborRow, neighborCol in getNeighbors(row, col):
                grid[neighborRow][neighborCol] = distance + 1
                queue.append((neighborRow, neighborCol))

        # no path was found to the end cell
        return -1
