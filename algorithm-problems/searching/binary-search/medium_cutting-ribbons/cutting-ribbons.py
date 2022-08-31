# LeetCode 1891. Cutting Ribbons
#
# Notes: use binary search to find the largest possible ribbon length by cutting
# k equaling length pieces from ribbons.
#
# Complexity:
# O(nlog(n)) time | O(1) space
from typing import List

class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        lo, hi = 0, max(ribbons) + 1
        while lo + 1 < hi:
            mid = (lo + hi) // 2
            if sum(r // mid for r in ribbons) >= k:
                lo = mid
            else:
                hi = mid
        return lo
