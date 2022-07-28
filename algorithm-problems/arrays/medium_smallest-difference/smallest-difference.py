# Notes:
# The brute-force approach uses a double nested loop to go through all possible
# pairs of numbers from the two arrays, and finds the smallest difference.
#
# Complexity:
# O(m * n) time | O(1) space - where m, n are the lengths of the arrays.
def smallestDifference(arrayOne, arrayTwo):
    smallestDiffPair = []
    for i in range(len(arrayOne)):
        for j in range(len(arrayTwo)):
            absDiff = abs(arrayOne[i] - arrayTwo[j])
            smallestAbsDiff = abs(smallestDiffPair[0] - smallestDiffPair[1]) if smallestDiffPair else float("inf")
            if absDiff < smallestAbsDiff:
                smallestDiffPair = [arrayOne[i], arrayTwo[j]]
    return smallestDiffPair

# In the optimal solution, we sort both arrays, set a pointer at the beginning
# of both the arrays, and compare the pairs of numbers at the pointers(denoted
# by x and y).
#
# If x < y, increment x so that next x might be closer to y; Similary, if y < x,
# increment y; If x = y, return the pair directly because the difference is 0.
# The loop continues until both indices reach the end of array, and we keep
# keep track of the smallest differnce.
#
# Complexity:
# The solution consist of two sorting steps, but does not use auxiliary data
# structure.
# O(nlog(n) + mlog(m)) time | O(1) space - wehre n and m are the length of the
# input arrays.
def smallestDifference(arrayOne, arrayTwo):
  # Assume we can use built-in sorting function, and the time complexity is
  # O(nlog(n))
  arrayOne.sort()
  arrayTwo.sort()
  # setup the pointers at the beginning of the arrays
  idxOne = 0
  idxTwo = 0
  # set up the smallest distance as positive infinity
  smallest = float("inf")
  current = float("inf")
  smallestPair = []
  # loop continues until both pinters have reached the end of the array.
  while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
    # this would be x
    firstNum = arrayOne[idxOne]
    # this would be y
    secondNum = arrayTwo[idxTwo]
    # calculate the difference and increment the appropriate pointer
    if firstNum < secondNum:
      current = secondNum - firstNum
      idxOne += 1
    elif secondNum < firstNum:
      current = firstNum - secondNum
      idxTwo += 1
    else:
      # if the difference is 0, return directly
      return [firstNum, secondNum]
    # keep track of the smallest difference
    if smallest > current:
      smallest = current
      smallestPair = [firstNum, secondNum]

  return smallestPair
