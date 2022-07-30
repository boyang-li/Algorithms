# Notes:
# Realise the fact that all the rows and columns are sorted, if we traverse the
# last column from top to bottom, if any element has a value larger than the
# target, we know every value in the rest of that column must be larger than the
# target. So, we can simply skip traversing the rest of the column.
#
# Similarly, it that element is smaller than the target, we can simply skip all
# the elements before that element in the same row as well.
#
# In this approach, we can find the target number within one single traversal of
# size of a row plus a column.
#
# Complexity:
# O(n + m) time | O(1) space - where m, n are the width and height of the matrix
def searchInSortedMatrix(matrix, target):
    row = 0
    col = len(matrix[0]) - 1
    # so long as our row and col pointers are in bounds, we continue
    while row < len(matrix) and col >= 0:
        if matrix[row][col] > target: # shift a column to the left
            col -= 1
        elif matrix[row][col] < target: # shift a row down
            row += 1
        else:
            return [row, col]
    return [-1, -1]
