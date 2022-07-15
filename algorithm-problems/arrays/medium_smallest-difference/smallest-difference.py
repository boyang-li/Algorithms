# brute-force approach - 2 loops, get every possible pairs of numbers, one from each array, and
# and the smallest absolute difference.
# 
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

# optimal solution - sort the arrays, set two pointers at the beginning of the arrays, and compare
# the pair of numbers, denoted by x, y - where x is the number pointer one currently poninnting to
# in array one, y is for array two.
#     - if x > y, we need to increment x to bring the two nums closer;
#     - if x < y, we need to increment y to bring the two nums closer;
#     - else x = y, the absolute difference between the two nums is 0, return it directly.
#
# O(nlog(n) + mlog(m)) time
def smallestDifference(arrayOne, arrayTwo):
  arrayOne.sort()
  arrayTwo.sort()
  idxOne = 0
  idxTwo = 0
  smallest = float("inf")
  current = float("inf")
  smallestPair = []
  while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
    firstNum = arrayOne[idxOne]
    secondNum = arrayTwo[idxTwo]
    if firstNum < secondNum:
      current = secondNum - firstNum
      idxOne += 1
    elif secondNum < firstNum:
      current = firstNum - secondNum
      idxTwo += 1
    else:
      return [firstNum, secondNum]
    if smallest > current:
      smallest = current
      smallestPair = [firstNum, secondNum]
  return smallestPair
