# Notes:
# we can solve this problem by iterating the input array in the reversed order,
# and swapping the values with the first three elements. We can do everything in
# place, so there is not need for auxiliary data structure.
#
# O(n) time | O(1) space - where n is the length of the array
def findThreeLargestNumbers(array):
    for i in reversed(range(len(array))):
        # third place
        if array[i] > array[2]:
            array[2], array[i] = array[i], array[2]
        elif array[i] == array[2]:
            # the 3rd place is taken, we've got a tie, so put it as the 2nd.
            array[1], array[i] = array[i], array[1]
        # second place
        if array[i] > array[1]:
            array[1], array[i] = array[i], array[1]
        elif array[i] == array[1]:
            # the 2nd place is taken, we've got a tie, so put it as the 1st.
            array[0], array[i] = array[i], array[0]
        # first place
        if array[i] > array[0]:
            array[0], array[i] = array[i], array[0]
    return array[:3]
