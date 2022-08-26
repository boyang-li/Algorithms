# Notes:
# Kadane's algorithm uses Dynamic Programming to allow only one pass of the
# array to find the max sum of the subarray ending at each of the indices, and
# then we can easily find the max sum of the entire array.
#
# Complexity:
# O(n) time | O(1) space - where n is the length of the input array
def kadanesAlgorithm(array):
    maxEndingHere = array[0]
    maxSoFar = array[0]
    for i in range(1, len(array)):
        num = array[i]
        maxEndingHere = max(num, maxEndingHere + num)
        maxSoFar = max(maxSoFar, maxEndingHere)
    return maxSoFar
