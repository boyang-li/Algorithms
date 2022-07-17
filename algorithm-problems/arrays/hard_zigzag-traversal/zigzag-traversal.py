# O(n) time | O(n) space - where n is the number of elements in the matrix
def zigzagTraverse(array):
    height = len(array) - 1
    width = len(array[0]) - 1
    result = []
    row, col = 0, 0
    goDown = True
    while not isOutOfBounds(row, col, height, width):
        # we are in bounds, so add the element to results
        result.append(array[row][col])
        if goDown:
            if col == 0 or row == height:
                # now change the direction for next iteration
                goDown = False
                if row == height:
                    # we hit the last row, must go right
                    col += 1
                else:
                    # we hit the left bound, go down along the col
                    row += 1
            else:
                row += 1
                col -= 1
        else:
            if row == 0 or col == width:
                goDown = True
                if col == width:
                    row += 1
                else:
                    col += 1
            else:
                row -= 1
                col += 1
    return result

def isOutOfBounds(row, col, height, width):
    return row < 0 or row > height or col < 0 or col > width
