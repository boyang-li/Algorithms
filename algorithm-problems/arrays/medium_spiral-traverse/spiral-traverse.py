# Notes:
# The standard solution involves constructing an output array of size m * n,
# traverse the matrix/2-D array in the spiral fashion, and fill up the output
# array on the go.
#
# Specifically, to traverse the matrix in spiral order, we set up a pair of
# pointers, horizontal(0 to (m - 1)) and vertical(0 to (n - 1)), to track the
# direction we are going as we advance in the matrix.
#
# we start by advancing to the right horizontally, when we have reached the end,
# we change the direction to advance to the bottom vertically, then to the left
# and finally to the top.
#
# Notice that the length of the pointers shorten every time it changes the
# direction. We keep going like this until we have filled up the output array.
#
# Complexity:
# O(m * n) time | O (m * n) space - where m is the width of the matrix, and n is
# the height of the matrix.
def spiralTraverse(array):
    if not array or not array[0]:
      return []

    n = len(array)
    m = len(array[0])
    outputArray = [0 for _ in range(n * m)]
    # important: note here we offset topBound by 1, because we start advancing
    # to the right horizontally where n = 0, so we do not want to overlap it
    # in the next cycle.
    leftBound, topBound = 0, 1
    rightBound, bottomBound = m - 1, n - 1
    direction = 1
    currIdx = 0
    i, j = 0, 0

    while currIdx < n * m:
      print('currIdx=', currIdx,'; i=', i, '; j=', j)
      # fill up the output as we go
      outputArray[currIdx] = array[i][j]
      print(outputArray)
      currIdx += 1
      # change direction
      if (direction == 1 and j == rightBound):
        # visited the right-most unvisited col for the first time
        direction = changeDirection(direction)
        rightBound -= 1
      elif (direction == 2 and i == bottomBound):
        # visited the bottom unvisited row for the first time
        direction = changeDirection(direction)
        bottomBound -= 1
      elif (direction == 3 and j == leftBound):
        # visited the left-most unvisited col for the first time
        direction = changeDirection(direction)
        leftBound += 1
      elif (direction == 4 and i == topBound):
        # visited the top unvisited row for the first time
        direction = changeDirection(direction)
        topBound += 1
      print('direction=', direction)
      # shift pointers
      if direction == 1:
        if j < rightBound: j += 1
      elif direction == 2:
        if i < bottomBound: i += 1
      elif direction == 3:
        if j > leftBound: j -= 1
      else:
        if i > topBound: i -= 1

    return outputArray

# directions: 1: left-right; 2: top-bottom; 3: right-left; 4: bottom-top
# directions are looped in the above order
def changeDirection(dir):
  if dir == 4:
    return 1
  else:
    return dir + 1

# Another optimal yet simpler solution which dose no require tracking direction
# is below: We set up two pairs of pointers for start/end rows and start/end
# columns at the extremeties of the matrix.
#
# Then we start looping until both pair of pointers pass each other. In other
# words, we have constructed a perimeter within the matrix, and it shrinks in
# each iteration until we have visited all of the elements in the matrix.
#
# Now within the first loop, we will have 4 independent nested loops, traversing
# the coloums from left to right, the rows from to to bottom, the columns from
# right to left, and the rows from bottom to top, resprectively.
#
# Note that the order of the traversals is important, and it is in the spiral
# order. We fill up the output array as we traverse the matrix.
def spiralTraverse(array):
    result = []
    # we set up the two pairs of pointers at the extremeties
    startRow, endRow = 0, len(array) - 1
    startCol, endCol = 0, len(array[0]) - 1

    # keep looping until either pair of bounds close up
    while startRow <= endRow and startCol <= endCol:
        # traverse to the right
        for col in range(startCol, endCol + 1):
            result.append(array[startRow][col])
        # traverse to the bottom, excluding startRow since we have visited it.
        for row in range(startRow + 1, endRow + 1):
            result.append(array[row][endCol])
        # traverse to left, excluding endCol since we have visited it.
        for col in reversed(range(startCol, endCol)):
            # if the horizontal bounds have closed up, stop the traversal
            if startRow == endRow:
                break
            result.append(array[endRow][col])
        # traverse to top, excluding endRow and startRow, since we have visited
        # both of them.
        for row in reversed(range(startRow + 1, endRow)):
            # if the vertical bounds have closed up, stop the traversal
            if startCol == endCol:
                break
            result.append(array[row][startCol])

        # update the pointers of bounds
        startRow += 1
        endRow -= 1
        startCol += 1
        endCol -= 1

    return result
