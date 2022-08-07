from collections import deque

# LeetCode 346. Moving Average from Data Stream
# Complexity:
# O(1) time | O(n) space - where n is the size of the moving window.
class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.windowQueue = deque()
        self.windowSum = 0
        self.count = 0

    def next(self, val: int) -> float:
        self.windowQueue.append(val)
        self.count += 1

        popVal = self.windowQueue.popleft() if self.count > self.size else 0
        self.windowSum = self.windowSum + val - popVal

        return self.windowSum / min(self.size, self.count)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)