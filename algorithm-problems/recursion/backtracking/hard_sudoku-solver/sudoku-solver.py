# LeetCode 37. Sudoku Solver
#
# Notes:
# This problem is a good fit for the "backtracking" technique.
# The algorithm can be broke down as follows:
# - Start from the upper left cell row = 0, col = 0. Proceed till the first free
#   cell i.e. a cell with value ".".
# - Iterate over the numbers from 1 to 9 and try to put each number 'num' in the
#   (row, col) cell.
#       - If number 'num' is not yet in the current row, column and subbox:
#           - Place the num in a (row, col) cell.
#           - Write down that num is now present in the current row, column and subbox.
#           - If we're on the last cell row == 8, col == 8:
#               - That means that we've solved the sudoku.
#           - Else
#               - Proceed to place further numbers.
#           - Backtrack if the solution is not yet here: remove the last number
#             from the (row, col) cell.
#
# Complexity:
# O((9!)ˆ9) time | O(9ˆ2) space
# time complexity - Time complexity is constant here since the board size is fixed
# and there is no N-parameter to measure. Let's consider one row, i.e. not more
# than 9 cells to fill. There are not more than 9 possibilities for the first
# number to put, not more than 9×8 for the second one, not more than 9×8×7 for
# the third one etc. In total that results in not more than 9! possibilities for
# a just one row, that means not more than (9!)^9 operations in total.
#
# space complexity - the board is fixed, and all the auxiliary data structures
# used have not more than 81 elements.
from typing import List
from collections import defaultdict

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # This function creates the solution board.
        def create_solution(board):
            ans_board = []
            for row in board:
                ans_board.append(row)
            return ans_board

        # This function maps given cell to the index of the list 'subBoxPlaced'.
        def mapSubboxIndex(row, col):
            return (row // n) * n + col // n

        def is_valid(row, col, num):
            return not (num in rowPlaced[row] or \
                num in colPlaced[col] or \
                num in subBoxPlaced[mapSubboxIndex(row, col)])

        # given an empty cell on the board, place a valid number in it
        def place_num(row, col, num):
            rowPlaced[row][num] += 1
            colPlaced[col][num] += 1
            subBoxPlaced[mapSubboxIndex(row, col)][num] += 1
            board[row][col] = str(num)

        def remove_num(row, col, num):
            del rowPlaced[row][num]
            del colPlaced[col][num]
            del subBoxPlaced[mapSubboxIndex(row, col)][num]
            board[row][col] = "."

        def place_next_num(row, col):
            if row == N - 1 and col == N - 1:
                nonlocal solved
                solved = True
            else:
                if col == N - 1:
                    backtrack(row + 1, 0)
                else:
                    backtrack(row, col + 1)

        # This function fills 3 lists of dicts holding the numbers that have
        # been placed in the board in terms of rows, cols and sub-boxes.
        def fill_placed(board):
            for row in range(N):
                for col in range(N):
                    if board[row][col] != ".":
                        num = int(board[row][col])
                        place_num(row, col, num)

        def backtrack(row = 0, col = 0):
            # iterate over all cells until the first empty cell
            if board[row][col] == ".":
                # iterate over number 1 to 9
                for n in range(1, 10):
                    if is_valid(row, col, n):
                        place_num(row, col, n)
                        place_next_num(row, col)

                        if not solved:
                            remove_num(row, col, n)
            else:
                place_next_num(row, col)

        # box size
        n = 3
        # board size
        N = n * n

        rowPlaced = [defaultdict(int) for i in range(N)]
        colPlaced = [defaultdict(int) for i in range(N)]
        subBoxPlaced = [defaultdict(int) for i in range(N)]
        fill_placed(board)

        # print(rowPlaced)
        # print(colPlaced)
        # print(subBoxPlaced)
        solved = False
        backtrack()
