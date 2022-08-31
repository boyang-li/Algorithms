# Notes:
# Binary Search only works when the input array is a sorted array of numbers.
# It works in a divide and conquer fashion, slicing the array in half in every
# iteration, and try to find the target number if either halves.
#
# Binary Search could be done in the recursive approach, but we do it the
# iterative way for better space complexity.
#
# In each iteration, we manipulate the left and right pointers, and navigate to
# the target by shifting the middle pointer around in place.
#
# Complexity
# O(log(n)) time | O(1) space - where n is the length of the input array.
def binarySearch(array, target):
    l = 0
    r = len(array) - 1
    while l <= r:
        if l == r:
            return l if array[l] == target else -1

        delta = (r - l + 1) // 2
        mid = l + delta
        if array[mid] == target: # we have found target
            return mid
        elif array[mid] > target: # target is smaller, shift mid to the left
            r = mid - 1
        elif array[mid] < target: # target is larget, shift mid to the right
            l = mid + 1
    return -1
