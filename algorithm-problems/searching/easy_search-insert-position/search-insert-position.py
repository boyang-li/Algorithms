# LeetCode 35. Search Insert Position
#
# Notes:
# Based on the description of the problem, we can see that it could be a good
# match with the binary search algorithm. But, what if the target value is not
# found? In this case, the loop will be stopped at the moment when left > right
# and nums[right] < target < nums[left]. Hence, the proper position to insert
# the target is at the index left.
#
# Complexity:
# O(log(n)) time | O(1) space
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # iterative binary search
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (right + left) // 2

            if nums[mid] == target:
                return mid

            if target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        # left is the proper position to insert if target is not found.
        return left
