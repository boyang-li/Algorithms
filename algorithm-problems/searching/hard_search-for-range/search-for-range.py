# Notes:
# The problem can be solved by a variation of the Binary Search. So in this
# problem, we are searching for a range of the same back-to-back target values.
#
# We run the Binary Search algorithm twice, once for searching the left
# extremity of the range, and once for searching the right extremetity of the
# range.
#
# We use a boolean flag to remind us which half to search for the next iteration
#
# We check the value next the middle to the direction we are going to see if it
# is equal to target, if not we know we have reached the extremety of the range.
#
# Complexity:
# O(log(n)) time | O(1) space - where n is the length of the input array.
def searchForRange(array, target):
    finalRange = [-1, -1]
    alteredBinarySearch(array, target, 0, len(array) - 1, finalRange, True)
    alteredBinarySearch(array, target, 0, len(array) - 1, finalRange, False)
    return finalRange

def alteredBinarySearch(array, target, left, right, finalRange, goLeft):
    while left <= right:
        mid = (left + right) // 2
        if array[mid] < target:
            left = mid + 1
        elif array[mid] > target:
            right = mid - 1
        else:
            if goLeft:
                if mid == 0 or array[mid - 1] != target:
                    finalRange[0] = mid
                    return
                else:
                    right = mid - 1
            else:
                if mid == len(array) - 1 or array[mid + 1] != target:
                    finalRange[1] = mid
                    return
                else:
                    left = mid + 1
