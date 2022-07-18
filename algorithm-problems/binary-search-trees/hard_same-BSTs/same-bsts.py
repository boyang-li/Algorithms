# O(nˆ2) time | O(nˆ2) space - where n is the number of elements in each array
def sameBsts(arrayOne, arrayTwo):
    # check if the two arrays are equal in length
    if len(arrayOne) != len(arrayTwo):
        return False

    # check for empty arrays
    if len(arrayOne) == 0 and len(arrayTwo) == 0:
        return True

    # check if the first elements are equal(root node)
    if arrayOne[0] != arrayTwo[0]:
        return False

    leftOne = getSmaller(arrayOne)
    leftTwo = getSmaller(arrayTwo)
    rightOne = getBiggerOrEqual(arrayOne)
    rightTwo = getBiggerOrEqual(arrayTwo)

    return sameBsts(leftOne, leftTwo) and sameBsts(rightOne, rightTwo)

# get the subarray with elements strictly smaller than the first element
def getSmaller(array):
    smaller = []
    for i in range(1, len(array)):
        if array[i] < array[0]:
            smaller.append(array[i])
    return smaller

# get the subarray with elements greater or equal to the first element
def getBiggerOrEqual(array):
    biggerOrEqual = []
    for i in range(1, len(array)):
        if array[i] >= array[0]:
            biggerOrEqual.append(array[i])
    return biggerOrEqual
