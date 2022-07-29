# Notes:
# Radix Sort involves calling Counting Sort multiple times(the number of digits
# of the largest number in the input array), and Counting Sort can be run in
# linear time. So, Radix Sort could potentially run faster than O(nlog(n)) time.
#
# Concretely, in each call of Counting Sort, we partially sort the input array
# based on one digit. We continuously sort the array based on the digit from
# the least significant digit to the leftmost digit of the largest number.
#
# After we finished sorting all the digits, the input array will be sorted.
#
# Complexity:
# Since the complexity for Counting Sort is: O(n + b) time | O(n + b) where n
# is the size of input array, and b is base of the numbering system, or the
# number of counts(e.g. base 10 system would results 10 number of counts: 0..9).
#
# O(d * (n + b)) time | O(n + b) space - where n is the length of the input
# array, d is the max number of digits, and b is the base of the numbering
# system.
def radixSort(array):
    if len(array) == 0:
        return array

    # find the largest number in the input array
    maxNumber = max(array)

    # start from the least significant digit and work the way up
    digit = 0
    # if the maximun number is divisible by 10 ** digit, the digit exists
    while maxNumber / (10 ** digit) > 0:
        # run Counting Sort on the digit
        countingSort(array, digit)
        # increment the digit
        digit += 1

    return array

# the Counting Sort function partially sorts the array based on the given digit.
def countingSort(array, digit):
    # create a new array for the partially sorted array
    sortedArray = [0] * len(array)
    # create a array for the counts
    countArray = [0] * 10

    # the denominator for digit extraction
    digitColumn = 10 ** digit
    # start counting the digit
    for num in array:
        # extract the digit from the number
        countIndex = (num // digitColumn) % 10
        # update digit count
        countArray[countIndex] += 1

    # for each digit counts, modify the elements in place such that they map to
    # the positions in the sorted array where we should place the numbers. The
    # The elements will be partially sorted based on the digit, and they are
    # placed from higher index to lower index if they have a tie in the digit.
    for idx in range(1, 10):
        countArray[idx] += countArray[idx - 1]

    # place the numbers in the sorted array in backward fashion due to the
    # "stable sorting property". Specifically, we want to avoid that elements
    # could be placed out of order when they were placed in sorted order in
    # previous Counting Sort call, but now are having a tie in the digit.
    for idx in range(len(array) - 1, -1, -1):
        # extract digit from the number
        countIndex = (array[idx] // digitColumn) % 10
        # decrement the count by one in the sense that we have used one of the
        # counts
        countArray[countIndex] -= 1
        # get the position in the sorted array for the number
        sortedIndex = countArray[countIndex]
        # place the number in the sorted array
        sortedArray[sortedIndex] = array[idx]

    # after we are done with placing the numbers, update the input array with
    # the partially sorted array(this improves space complexity as we are
    # sorting in place).
    for idx in range(len(array)):
        array[idx] = sortedArray[idx]
