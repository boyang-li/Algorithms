# O(n) time | O(1) space - where n is the length of the array
def findThreeLargestNumbers(array):
    for i in reversed(range(len(array))):
        # third place
        if array[i] > array[2]:
            array[2], array[i] = array[i], array[2]
        elif array[i] == array[2]:
            array[1], array[i] = array[i], array[1]
        # second place
        if array[i] > array[1]:
            array[1], array[i] = array[i], array[1]
        elif array[i] == array[1]:
            array[0], array[i] = array[i], array[0]
        # third place
        if array[i] > array[0]:
            array[0], array[i] = array[i], array[0]
    return array[:3]
