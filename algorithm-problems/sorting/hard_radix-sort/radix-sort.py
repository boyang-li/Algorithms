# Radix Sort/Bucket Sort
# O(d * (n + b)) time | O(n + b) space - where n is the length of the input array,
# d is the max number of digits, and b is the base of the numbering system.
# Note that the complexity for counting sort is: O(n + b) time | O(n + b)
def radixSort(array):
    if len(array) == 0:
        return array

    maxNumber = max(array)

    # we start from the least significant digit in the numbers,
    # if the maximun number is divisible by 10 ** digit, it means
    # that number has the digit and we can do counting sort
    digit = 0
    while maxNumber / (10 ** digit) > 0:
        countingSort(array, digit)
        digit += 1

    return array

def countingSort(array, digit):
    # having an array to store partialy sorted numbers
    sortedArray = [0] * len(array)
    # having a array for digit counts
    countArray = [0] * 10

    digitColumn = 10 ** digit
    # start counting the digit
    for num in array:
        # extract the digit we are looking for from the number
        countIndex = (num // digitColumn) % 10
        # update the count based on the digit
        countArray[countIndex] += 1

    # loop throught the count array, modify the elements such that we know
    # where the furthest right position is that we should be placing the numbers
    # in the sorted array
    for idx in range(1, 10):
        countArray[idx] += countArray[idx - 1]

    # placing the numbers in the sorted array
    # *note* make sure we maintain the "stable sorting property"
    # by looping backwards
    for idx in range(len(array) - 1, -1, -1):
        # again, extract digit from the number
        countIndex = (array[idx] // digitColumn) % 10
        # decrement the count by one
        countArray[countIndex] -= 1
        # get the position to place the number
        sortedIndex = countArray[countIndex]
        # place the number in the sorted array
        sortedArray[sortedIndex] = array[idx]

    # once we are done placing all the numbers in the sorted array,
    # replace the input array with the sorted array(for space complexity improvement).
    for idx in range(len(array)):
        array[idx] = sortedArray[idx]
