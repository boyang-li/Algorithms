# Notes:
# The brute-force approach uses a triple nested loop, we go through all possible
# triplets, and find the ones that sum up to targetSum. We have to make sure
# no duplicate is added, and the triplet elements are ascendingly ordered. This
# approach would have a Time Complexity of O(nˆ3).
#
# Better approach is to first sort the array, and construct a double nested
# loop to go through each element of the array in order. In each iteration, we
# find the rest of the array, and set up two pointers at the left and right
# extremities, then uses a second loop to bring left and right to each other.
#
# In the nested loop, we calculate the sum of Array[i], Array[left] and
# Array[right], and add the triplet to the output whenever we finf a match, and
# continue the loop until left passes right.
#
# We take the advantage of the fact that the array is sorted, and increment left
# or decrement right to make the sum closer to targetSum. Naturally, the numbers
# in the triplets will always be in ascending order, and free of duplicates.
#
# Complexity:
# We have a double nested loop, and an auxiliary data structure of size n for
# the outout.
# O(n^2) time | O(n) space - where n is the length of the input array.
def threeNumberSum(array, targetSum):
    # assume we could use the built-in sorting function.
    array.sort()
    triplets = []
    # the loop stops at the 3rd element from the end, so that we won't go out of
    # bound when we calculate a triplet.
    for i in range(len(array) - 2):
        left = i + 1
        right = len(array) - 1
        # the loop stops when left completely passes right
        while left < right:
            # sum of the triplet
            currSum = array[i] + array[left] + array[right]
            # we found a match
            if currSum == targetSum:
                triplets.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            # under targetSum, increment left by 1 to make sum larger
            elif currSum < targetSum:
                left += 1
            # over targetSum, decrement right by 1 to make sum smaller
            elif currSum > targetSum:
                right -= 1

    return triplets
