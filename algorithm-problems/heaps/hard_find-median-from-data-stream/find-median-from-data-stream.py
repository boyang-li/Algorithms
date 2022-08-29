# LeetCode 295. Find Median from Data Stream

# Notes:
# we maintain two heaps with roughly the same size, heap 'large' is a MinHeap
# and heap 'small' is a MaxHeap. Every number in the large head is larger than
# the numbers in the small heap. By having this setup, we can easily calculate
# the median by taking the minimum of the large heap(odd size, large heap is
# greater in size), the maximum of the small heap(odd size, small heap is
# greater in size), or take the average of the both(even size, both heaps are
# equal in size).
#
# Complexity:
# Time
# - Adding a number takes amortized O(1) time for a container with an efficient
# resizing scheme.
# - Finding the median is primarily dependent on the sorting that takes place.
# This takes O(nlogn) time for a standard comparative sort.
# Space
# linear space to hold input in a container. No extra space other than that
# needed (since sorting can usually be done in-place).
# O(nlogn) time | O(n) space
import heapq

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        # two heaps, large, small, minheap, maxheap
        # heaps should be equal size
        self.small, self.large = [], []


    def addNum(self, num: int) -> None:
        # since python only has MinHeap, and 'small' needs to be a MaxHeap,
        # we multiply every number by -1 to effectively implement a MaxHeap.
        heapq.heappush(self.small, -1 * num)

        # make sure every num small is <= every num in large
        if (self.small and self.large and
            ( -1 * self.small[0]) > self.large[0]):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # uneven size?
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]

        return (-1 * self.small[0] + self.large[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
