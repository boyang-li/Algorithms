# Notes:
# The naive approach for this prblem would probablly involve keeping track of
# the direction of the trend, so that we know whether the values are monotonic
# based in the existence of change in directions.
#
# The simpler solution is rather more clever. It uses two flags to keep track of
# wheter the values are non-decreasing, and are non-increasing at the same time.
# So long as the two flags do not turn to be True at the same time, we know that
# the trend did not change, in other words, values are monotonic.
#
# Complexity:
# We can solve this by iterating the array once, and we do not need auxiliary
# data structure.
# O(n) time | O(1) space - where n is the length of the array.
def isMonotonic(array):
  # set up the two flags
  isNonDecreasing = True
  isNonIncreasing = True
  # loop through the array
  for i in range(1, len(array)):
    # check adjacent elements for decreasing trend
    if array[i] < array[i - 1]:
      isNonDecreasing = False
    # check adjacent elements for increasing trend
    if array[i] > array[i - 1]:
      isNonIncreasing = False

  # the crusial argument that checks whether a change of direction has occurred.
  return isNonDecreasing or isNonIncreasing
