# Notes:
# The solution start by setting up two pointers at the left and right
# extremeties, and uses a loop to bring them to each other. As long as left
# has not passed right.
#
# We compare values at left and right to the value to move to end, we keep
# decrementing right until we do not see a match, and we swap left and right
# elements whenever we found match for left.
#
# When we finished the loop, we have effectively moved all the target elements
# to the end of the array in place.
#
# Complexity:
# The algorithm uses a double nested loop, but we would never visit the same
# element twice, and we do not need auxiliary data structure.
# O(n) time | O(1) space - n is the length of the array.
def moveElementToEnd(array, toMove):
  # set up pointers at the left and right extremities
  l, r = 0, len(array) - 1

  # continue until left has completely passed right
  while l < r:
    # find the first value that is not equal to the target from the end. It will
    # be the position for the next swap.
    # the check for i < j is very important!
    while l < r and array[j] == toMove:
        l -= 1
    # swap left and right whenever a match is found for left
    if array[l] == toMove:
      array[l], array[r] = array[r], array[l]
    l += 1

  return array
