# O(nlog(n)) time | O(1) space - where n is the length of the array
# note that the two input arrays are the same in length.
# the catch: here the greedy choice is that in each iteration,
# we pick the tallest student to place into the row.
#
# tips: make sure to ask if we could mutate the arrays.
def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort(reverse=True)
    blueShirtHeights.sort(reverse=True)

    shirtColorInFirstRow = 'RED'if redShirtHeights[0] < blueShirtHeights[0] else 'BLUE'
    for i in range(len(redShirtHeights)):
        redShirtHeight = redShirtHeights[i]
        blueShirtHeight = blueShirtHeights[i]

        if shirtColorInFirstRow == 'RED':
            if redShirtHeight >= blueShirtHeight:
                return False
        else:
            if blueShirtHeight >= redShirtHeight:
                return False

    return True
