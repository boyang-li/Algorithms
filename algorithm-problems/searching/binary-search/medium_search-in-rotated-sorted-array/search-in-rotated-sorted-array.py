# LeetCode 33. Search in Rotated Sorted Array
#
# Notes:
# We could achieve the goal in one pass with an revised binary search.
# The idea is that we add some additional condition checks in the normal binary
# search in order to better narrow down the scope of the search.
#
# As in the normal binary search, we keep two pointers (i.e. start and end) to
# track the search scope. At each iteration, we reduce the search scope into
# half, by moving either the start or end pointer to the middle (i.e. mid) of
# the previous search scope.
#
# Initiate the pointer start to 0, and the pointer end to n - 1. Perform
# standard binary search. While start <= end:
#    - Take an index in the middle mid as a pivot.
#    - If nums[mid] == target, the job is done, return mid.
#    - Now there could be two situations:
#       1. Pivot element is larger than the first element in the array, i.e. the
#          subarray from the first element to the pivot is non-rotated, as shown
#          in the following graph.
#           - If the target is located in the non-rotated subarray:
#             go left: `end = mid - 1`.
#           - Otherwise: go right: `start = mid + 1`.
#       2. Pivot element is smaller than the first element of the array, i.e.
#          the rotation index is somewhere between 0 and mid. It implies that
#          the sub-array from the pivot element to the last one is non-rotated,
#          as shown in the following graph.
#           - If the target is located in the non-rotated subarray:
#             go right: `start = mid + 1`.
#           - Otherwise: go left: `end = mid - 1`.
#
# Complexity:
# O(logn) time | O(1) space

from typing import List

def search(nums: List[int], target: int) -> int:
    start, end = 0, len(nums) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] >= nums[start]:
            if target >= nums[start] and target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if target <= nums[end] and target > nums[mid]:
                start = mid + 1
            else:
                end = mid - 1
    return -1
