# Brute-force approach: having triple nested loops, and try to
# find every possible triplet that add up to the target sum.
# Meanwhile, we still have to make sure no to include duplicates and
# maintain the ascending order in the triplets.
#
# Better approach: sort the array of integers in ASC order.
# start by looping thourgh the sorted array, for each integer,
# set up a left pointer and a right pointer at the indices i+1
# and (len(array)-1) such that the three elements in a potential
# matching triplet would be represented by the values at i, let and
# right(natualy in ASC order due to the sorted array).
#
# Then within that iteration, we start a nested loop to increment
# the left pointer or to decrement the right pointer based on
# the sum of the three integers, and we continue as long as the left
# and right do not pass each other. Whenever the three integers add up
# to the targetSum, we add a tripplet to our output. By this setup,
# we are guranteed to have the triplets in ASC order and free of
# duplicates.
# O(n^2) time | O(n) space - where n is the length of the input array.
def threeNumberSum(array, targetSum):
    array.sort()
    triplets = []
    # we stop at the 3rd last number because we need to make
    # space for the left and right pointers
    for i in range(len(array) - 2):
        left = i + 1
        right = len(array) - 1
        while left < right:
            currSum = array[i] + array[left] + array[right]
            if currSum == targetSum:
                triplets.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif currSum < targetSum:
                left += 1
            elif currSum > targetSum:
                right -= 1
    return triplets
