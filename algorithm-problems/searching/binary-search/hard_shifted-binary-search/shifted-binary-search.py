# Notes:
# Unlike the vanilla Binary Search, the input array could be shifted, so a
# portion of the array could be out of order.
#
# Similiar to the Binary Search, we still divide the array in half and look at
# one of them. But, we need to first check if the half is sorted. Realise the
# fact that if one half is not sorted, the other half must be sorted by setup.
#
# We would always want to look at the sorted half first, and check whether the
# target number is in that half by comparing the target with the two numbers
# at the bounds of the sorted half. And if it is not in the sorted half, it must
# be in the unsorted other half.
#
# Complexity:
# O(log(n)) time | O(log(n)) space - where n is the length of the input array.
def shiftedBinarySearch(array, target):
    return shiftedBinarySearchHelper(array, target, 0, len(array) - 1)

def shiftedBinarySearchHelper(array, target, left, right):
    if left > right:
        return -1
    mid = (left + right)//2
    midNum = array[mid]
    leftNum = array[left]
    rightNum = array[right]
    if target == midNum:
        return mid
    elif leftNum <= midNum: # the left half is sorted
        if target < midNum and target >= leftNum: # target is in the left half
            return shiftedBinarySearchHelper(array, target, left, mid - 1)
        else: # target is in the right half
            return shiftedBinarySearchHelper(array, target, mid + 1, right)
    else: # the left half is not sorted, the right half must be sorted
        if target > midNum and target <= rightNum: # target is in the right half
            return shiftedBinarySearchHelper(array, target, mid + 1, right)
        else: # target is in the left half
            return shiftedBinarySearchHelper(array, target, left, mid - 1)

# The iterative version is very similiar to the recursive version, instead of
# recursive calls, it simply updates the pointers. There is no extra space
# taken on the recursive call stack, so the space complexity is constant.
#
# Complexity:
# O(log(n)) time | O(1) space
def shiftedBinarySearch(array, target):
    return shiftedBinarySearchIter(array, target, 0, len(array) - 1)

def shiftedBinarySearchIter(array, target, left, right):
    while left <= right:
        mid = (left + right) // 2
        midNum = array[mid]
        leftNum = array[left]
        rightNum = array[right]
        if target == midNum:
            return mid
        elif leftNum <= midNum:
            if target < midNum and target >= leftNum:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if target > midNum and target <= rightNum:
                left = mid + 1
            else:
                right = mid - 1
    return -1
