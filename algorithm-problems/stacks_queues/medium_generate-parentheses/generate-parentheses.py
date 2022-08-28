# LeetCode 22. Generate Parentheses
#
# Notes:
# Use the recursive approach to solve it. Only add parenthesis when we know it
# will remain a valid sequence. We can do this by keeping track of the number of
# opening and closing brackets we have placed so far.
#
# We can start an opening bracket if we still have one (of n) left to place. And
# we can start a closing bracket if it would not exceed the number of opening
# brackets.
#
# Complexity:
# Our complexity analysis rests on understanding how many elements there are in
# generateParenthesis(n). It turns out this is the n-th Catalan number which is
# is bounded asymptotically by 4ˆn/(n * sqrt(n))
#
# O(4ˆn/sqrt(n)) time | O(4ˆn/sqrt(n)) space

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # only add open paranthesis if open < n
        # only add a closing paranthesis if closed < open
        # valid IIF open == closed == n

        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()

            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0, 0)
        return res
