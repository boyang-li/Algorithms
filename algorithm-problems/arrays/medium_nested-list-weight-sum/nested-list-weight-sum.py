# LeetCode 339. Nested List Weight Sum
#
# Notes:
# The nested list is usually a sign to use recursion. For this problem, we have
# two approaches: DFS and BFS. The DFS uses recursion, whereas the BFS uses
# a loop to pop a queue until it is empty.
#
# Complexity(DFS):
# for space complexity, there are d(max depth) recursive calls on the stack, and
# the worst case is that d = n.
# O(n) time | O(n) space - where n is the number of elements in the nested list,
# and d is the maximum depth of the nested list.
from collections import deque

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:

        def depthSumHelper(item, depth):
            total = 0
            for ele in item:
                if ele.isInteger():
                    total += ele.getInteger() * depth
                else:
                    total += depthSumHelper(ele.getList(), depth + 1)

            return total

        return depthSumHelper(nestedList, 1)

# Complexity(BFS):
# for space complexity, the queue stores all the elements in the flatten nested
# list, which consist of n elements. for time complexity, each elements in the
# queue is visited exactly once.
# O(n) time | O(n) space - where n is the number of elements in the nested list,
# and d is the maximum depth of the nested list.
class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        queue = deque(nestedList)

        total = 0
        depth = 1

        while len(queue) > 0:
            for i in range(len(queue)):
                item = queue.pop()
                if item.isInteger():
                    total += item.getInteger() * depth
                else:
                    queue.extendleft(item.getList())
            depth += 1

        return total

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
