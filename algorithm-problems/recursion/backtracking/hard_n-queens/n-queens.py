# LeetCode 51. N-Queens
#
# Notes:
# This problem can be solved using the "backtrack" paradigm, which is often
# implemented in recursion. It is general algorithm for finding all(or some)
# solutions to some computational problems, which incrementally builds
# candidates to the solution and abandons a candidate("backtrack") as soon as
# it determines that the candidate cannot lead to a valid solution.
#
# n-queens problem break-down:
# 1.Overall, we iterate over each row in the board, i.e. once we reach the
#   last row of the board, we should have explored all the possible solutions.
# 2.At each iteration, further iterate over each column of the board along
#   current row. At this second iteration, we then can explore the possibility
#   of placing a queen on a particular cell.
# 3.Before, we place a queen on the cell with index(now, col), we check if
#   if this cell is under the attacking zone of the queens that have been placed
#   on the board before.
# 4.Once the check passes, we then can proceed to place a queen. Along with the
#   placement, one should also mark out the attacking zone of this newly-placed
#   queen.
# 5.As an important behaviour of backtracking, we should be able to abandon our
#   previous decision at the moment we decide to move on to the next candidate.
#
# Complexity:
# O(n!) time | O(nˆ2)
# time complexity - For the first queen, we have N options.  For the next queen,
# we won't attempt to place it in the same column as the first queen, and there
# must be at least one square attacked diagonally by the first queen as well.
# Thus, the maximum number of squares we can consider for the second queen is N−2.
# For the third queen, we won't attempt to place it in 2 columns already occupied
# by the first 2 queens, and there must be at least two squares attacked diagonally
# from the first 2 queens. Thus, the maximum number of squares we can consider
# for the third queen is N−4. This pattern continues, resulting in an approximate
# time complexity of N!.
#
# space complexity - Extra memory used includes the 3 sets used to store board
# state, as well as the recursion call stack. All of this scales linearly with
# the number of queens. However, to keep the board state costs O(N^2), since the
# board is of size N * N. Space used for the output does not count towards space
# complexity.
from typing import List

def solveNQueens(n: int) -> List[List[str]]:
    def create_board(state):
        board = []
        for row in state:
            board.append("".join(row))
        return board

    def is_under_attack(row, col, diagonals, anti_diagonals, cols):
        curr_diagonal = row - col
        curr_anti_diagonal = row + col
        # if the queen is not placeable
        if (col in cols
                or curr_diagonal in diagonals
                or curr_anti_diagonal in anti_diagonals):
            return True
        return False

    def place_queen(row, col, diagonals, anti_diagonals, cols, state):
        curr_diagonal = row - col
        curr_anti_diagonal = row + col
        # 'add' the queen to the board
        cols.add(col)
        diagonals.add(curr_diagonal)
        anti_diagonals.add(curr_anti_diagonal)
        state[row][col] = "Q"

    def remove_queen(row, col, diagonals, anti_diagonals, cols, state):
        curr_diagonal = row - col
        curr_anti_diagonal = row + col
        # 'remove' the queen from the board since we have already
        # explored all valid paths using the above function call
        cols.remove(col)
        diagonals.remove(curr_diagonal)
        anti_diagonals.remove(curr_anti_diagonal)
        state[row][col] = "."

    def backtrack(row, diagonals, anti_diagonals, cols, state):
        # base case - N queens have been palced
        if row == n:
            ans.append(create_board(state))
            return

        for col in range(n):
            if is_under_attack(row, col, diagonals, anti_diagonals, cols):
                continue
            # place the queen if it is not in attacking zone of existing queens
            place_queen(row, col, diagonals, anti_diagonals, cols, state)
            # move on to the next row with the updated board state
            backtrack(row + 1, diagonals, anti_diagonals, cols, state)
            # backtrack
            remove_queen(row, col, diagonals, anti_diagonals, cols, state)

    ans = []
    empty_board = [["."] * n for _ in range(n)]
    backtrack(0, set(), set(), set(), empty_board)
    return ans
