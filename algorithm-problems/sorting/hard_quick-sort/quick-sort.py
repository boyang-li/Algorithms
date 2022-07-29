# Notes:
# QuickSort involves recursion, in each recursive call we choose a random index
# as the 'pivot'(for this implementation we always choose the first index for
# simplicity), then we set up a pair of pointers at the left and right
# extremeties of the rest of the array.
#
# We keep iterating to bring left and right to the middle until they eventually
# pass each other. We compare the values at the left and right pointers with
# the pivot such that:
#    if left > pivot and right < pivot, then swap values at left and right;
#    if left <= pivot, increment the left pointer by one;
#    if right >= pivot, decrement the right pointer by one;
#
# Once we are done with the swapping and shifting, we finally swap the values at
# the pivot and the right pointer, so the pivot value is in its sorted position.
#
# We call the function recursively on the two halves separated by right pointer.
# Note that we call it on the smaller half first for performance considerations.
#
# Complexity:
# Best: O(nlog(n)) time | O(log(n)) space
# Average: O(nlog(n)) time | O(log(n)) space
# Worst: O(n^2) time | O(log(n)) space
def quickSort(array):
    quickSortHelper(array, 0, len(array) - 1)
    return array

def quickSortHelper(array, start, end):
    # check whether the start and end indices are in bounds
    if start >= end:
        return
    # we always choose the first index as the pivot
    pivot = start
    # set up the left and right pointers at the extremeties of the rest of array
    left = start + 1
    right = end
    # keep looping until left passes right
    while left <= right:
        # left and right are out of position, swap them
        if array[left] > array[pivot] and array[right] < array[pivot]:
            swap(left, right, array)
        # left is in position, increment left
        if array[left] <= array[pivot]:
            left += 1
        # right is in position, decrement right
        if array[right] >= array[pivot]:
            right -= 1
    # realise that we swap the pivot and right, pivot would be in position
    swap(pivot, right, array)
    # check wheter the left half is the smaller than the right half,
    # the two halves are separated by the right pointer. The order for
    # the recursive calls is that the smaller half goes before the larger half.
    leftSubarrayIsSmaller = right - 1 - start < end - right + 1
    if leftSubarrayIsSmaller:
        quickSortHelper(array, start, right - 1)
        quickSortHelper(array, right + 1, end)
    else:
        quickSortHelper(array, right + 1, end)
        quickSortHelper(array, start, right - 1)

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
