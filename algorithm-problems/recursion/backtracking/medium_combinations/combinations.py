# LeetCode 77. Combinations
#
# Notes:
# This problem can be solved with the "backtracking" technique.
# The algorithm can be broke down as following:
# - If the current combination is done - add it to output.
# - Iterate over the integers from 'first' to 'n'.
#   - Add integer i into the current combination list.
#   - Proceed to add more integers into the combination: backtrack(i + 1, curr).
#   - Backtrack by removing i from the current combination list.
#
# Complexity:
# O(k * n!/(n-k)!k!) time | O(n!/(n-k)!k!) - where Cnk = n!/(n-k)!k! is a
# number of combinations to build, and we are appending the built combination
# of length k to the result.
from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(first = 1, curr_comb = []):
            # if the combination is done
            if len(curr_comb) == k:
                result.append(curr_comb[:])
            for i in range(first, n + 1):
                # add i to the current combination
                curr_comb.append(i)
                # use next integers to complete the combination
                backtrack(i + 1, curr_comb)
                # backtrack
                curr_comb.pop()

        result = []
        backtrack()
        return result
