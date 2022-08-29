# LeetCode 853. Car Fleet

# Notes:
# We want to loop the cars in reverse sorted order, and use a stack to store
# potential car fleets.
#
# Complexity:
# O(n) time | O(n) space
from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p, s] for p, s in zip(position, speed)]

        stack = []
        for p, s in sorted(pair)[::-1]: # Reverse sorted order
            # push the time for this car to get to destination to the stack
            stack.append((target - p) / s)
            # whenever the stack has at least 2 elements, compare if the last
            # car's time required is shorter than the second last car, which
            # implies that the second car will get blocked and they form a fleet
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                # since we go reverse order, all the cars collide with the car
                # before it are already checked, so pop them as they are now
                # counted as the same fleet with its leader
                stack.pop()
        return len(stack)
