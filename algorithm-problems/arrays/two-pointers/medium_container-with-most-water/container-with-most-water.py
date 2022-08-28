# LeetCode 11. Container With Most Water

from typing import List

class Solution:
    # Brute force approach
    # O(nˆ2) time | O(1) space
    def maxAreaNaive(self, height: List[int]) -> int:
        maxarea = 0
        for left in range(len(height)):
            for right in range(left + 1, len(height)):
                width = right - left
                maxarea = max(maxarea, min(height[left], height[right]) * width)

        return maxarea

    # Two pointer approach
    #
    # Notes:
    # Initially we consider the area constituting the exterior most lines. Now, to
    # maximize the area, we need to consider the area between the lines of larger
    # lengths. If we try to move the pointer at the longer line inwards, we won't
    # gain any increase in area, since it is limited by the shorter line. But moving
    # the shorter line's pointer could turn out to be beneficial, as per the same
    # argument, despite the reduction in the width. This is done since a relatively
    # longer line obtained by moving the shorter line's pointer might overcome the
    # the reduction in area caused by the width reduction.
    #
    # Complexity:
    # O(n) time | O(1) space
    def maxArea(self, height: List[int]) -> int:
        maxarea = 0
        left = 0
        right = len(height) - 1

        while left < right:
            width = right - left
            maxarea = max(maxarea, min(height[left], height[right]) * width)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return maxarea
