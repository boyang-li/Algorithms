# O(n + m) time | O(1) space - where m, n are the width and height of the matrix
def searchInSortedMatrix(matrix, target):
    row = 0
    col = len(matrix[0]) - 1
    # so long as our row and col pointers are in bounds
    while row < len(matrix) and col >= 0:
        if matrix[row][col] > target:
            col -= 1
        elif matrix[row][col] < target:
            row += 1
        else:
            return [row, col]
    return [-1, -1]
