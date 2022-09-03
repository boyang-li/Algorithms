# LeetCode 79. Word Search
#
# Notes:
# We use the backtracking method to solve this problem. We implement this
# backtrack() as a recursive function, and it can be broke down to the following
# steps:
# 1.At the beginning, first we check if we reach the bottom case of the
# recursion, where the word to be matched is empty, i.e. we have already found
# the match for each prefix of the word.
#
# 2.We then check if the current state is invalid, either the position of the
# cell is out of the boundary of the board or the letter in the current cell
# does not match with the first letter of the word.
#
# 3.If the current step is valid, we then start the exploration of backtracking
# with the strategy of DFS. First, we mark the current cell as visited, e.g. any
# non-alphabetic letter will do. Then we iterate through the four possible
# directions, namely up, right, down and left. The order of the directions can
# be altered, to one's preference.
#
# 4.At the end of the exploration, we revert the cell back to its original state.
# Finally we return the result of the exploration.
#
# Complexity:
# O(n * 3ˆL) time | O(L) space - where n is the number of cells in the board and
# L is the length of the word to be matched.
#
# time complexity - or the backtracking function, initially we could have at
# most 4 directions to explore, but further the choices are reduced into 3. As a
# result, the execution trace after the first step could be visualized as a
# 3-ary tree, each of the branches represent a potential exploration in the
# corresponding direction. Therefore, in the worst case, the total number of
# invocation would be the number of nodes in a full 3-nary tree, which is about
# 3^L.
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.ROWS = len(board)
        self.COLS = len(board[0])
        self.board = board

        for row in range(self.ROWS):
            for col in range(self.COLS):
                if self.backtrack(row, col, word):
                    return True

        # no match found after all exploration
        return False

    def backtrack(self, row, col, suffix):
        # bottom case: we find match for each letter in the word
        if len(suffix) == 0:
            return True

        # Check the current status, before jumping into backtracking
        if row < 0 or row == self.ROWS or col < 0 or col == self.COLS \
                or self.board[row][col] != suffix[0]:
            return False

        # mark the choice before exploring further.
        self.board[row][col] = '#'
        # explore the 4 neighbor directions
        for rowOffset, colOffset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if self.backtrack(row + rowOffset, col + colOffset, suffix[1:]):
                return True

        # revert the change, a clean slate and no side-effect
        self.board[row][col] = suffix[0]

        # Tried all directions, and did not find any match
        False
