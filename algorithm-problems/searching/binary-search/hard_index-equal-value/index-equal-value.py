# Notes:
# The brute-force approach to solve this problem is to simply iterate the
# input array, once we have found a value that is equal to its index, we are
# done. This would run in O(n) time.
#
# The fact that the array is sorted and the values are distinct tell us that we
# could do better than linear time.
#
# We can solve it using a alteration of Binary Search. We set up a pair of
# pointers, left and right, at the extremeties of the array. Then start to
# iterate to bring them to middle until they pass each other. In each iteration,
# we divide the array in half, and check the middle index to determine where the
# next left, right, and middle pointers go to.
#
# Realise the fact that the array is sorted, it tells us if the value at index i
# is smaller than i, then every single value to its left must be smaller than
# its index. This holds true for every value to the right of the value which is
# greater than its index as well. In this case, we can simply ignore all the
# values to its left/right.
#
# Complexity:
# O(log(n)) time | O(1) space
#
def indexEqualsValue(array):
    leftIdx = 0
    rightIdx = len(array) - 1

    while leftIdx <= rightIdx:
        midIdx = leftIdx + (rightIdx - leftIdx)//2
        midVal = array[midIdx]

        if midVal < midIdx:
            # every value to the left of middle index can be ignored, we can do
            # it by simply iterate to the right half.
            leftIdx = midIdx + 1
        elif midVal == midIdx and midIdx == 0:
            # we found a match of index-equal-value and the index is the left
            # extremety, we are done.
            return midIdx
        elif midVal == midIdx and array[midIdx - 1] < midIdx - 1:
            # we found a match of index-equal-value and the very next value to
            # its left is a value smaller that its index, it means our current
            # index-equal-value must be the first in the array.
            return midIdx
        else:
            # every value to the right of middle index can be ignored, we can do
            # it by simply iterate to the left half.
            rightIdx = midIdx - 1

    return -1
