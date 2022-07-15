# intuition - construct an array of size m * n, traverse the matrix in spiral fashion, and
# insert the values to the array in order.
# 
# To traverse the matrix in spiral order, we keep track of two pointers for 0to(m-1) and 0to(n-1),
# we start off by increment the pointer for 0to(m-1) by one first, once it reaches the end, we
# immediately start to increment the pointer for 0to(n-1) by one. When the second pointer reaches
# the end, we then start to decrement the first pointer by one, then decrement the second pointer
# by one. We keep going like this until we have filled up the output array.
#
# O(m * n) time | O (m * n) space
def spiralTraverse(array):
    if not array or not array[0]:
      return []

    n = len(array)
    m = len(array[0])
    outputArray = [0 for _ in range(n * m)]
    # important: note here we offset topBound by 1, because
    # we start along it so we do not want to reach it again
    # in the next round.
    leftBound, topBound = 0, 1
    rightBound, bottomBound = m - 1, n - 1
    direction = 1
    nextDirection = 1
    currIdx = 0
    i, j = 0, 0
    
    while currIdx < n * m:
      print('currIdx=', currIdx,'; i=', i, '; j=', j)
      # insert value
      outputArray[currIdx] = array[i][j]
      print(outputArray)
      currIdx += 1
      # change direction
      if (direction == 1 and j == rightBound):
        direction = changeDirection(direction)
        rightBound -= 1
      elif (direction == 2 and i == bottomBound):
        direction = changeDirection(direction)
        bottomBound -= 1
      elif (direction == 3 and j == leftBound):
        direction = changeDirection(direction)
        leftBound += 1
      elif (direction == 4 and i == topBound):
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

# A more clever solution with optimal complexity as well,
# in this solution we do not need to keep track of directions.
def spiralTraverse(array):
    result = []
    startRow, endRow = 0, len(array) - 1
    startCol, endCol = 0, len(array[0]) - 1

    while startRow <= endRow and startCol <= endCol:
        for col in range(startCol, endCol + 1):
            result.append(array[startRow][col])

        for row in range(startRow + 1, endRow + 1):
            result.append(array[row][endCol])

        for col in reversed(range(startCol, endCol)):
            if startRow == endRow:
                break
            result.append(array[endRow][col])

        for row in reversed(range(startRow + 1, endRow)):
            if startCol == endCol:
                break
            result.append(array[row][startCol])

        startRow += 1
        endRow -= 1
        startCol += 1
        endCol -= 1

    return result