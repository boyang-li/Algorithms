# Notes:
# We use two pointers to slice the input array into appraopriate substrings,
# and push them in to the result array in reversed order. To determine the
# appropriate locations to slice the array, we check whether the values at the
# two pointers are in the following conditions:
#
# 1. the start is at a non-space character, but the end is at a space;
# 2. the start is at a space, but the end is at a non-space character;
#
# Note that we are shifting the end pointer by 1 position at a time, and only
# shifting the start pointer directly to the end poiner's position at the time
# of the slice. Therefore, every time either of the above conditions is met, it
# is the moment a word begins or ends, and it is the time we should slice the
# array and add it the the result.
#
# Complexity:
# O(n) time | O (n) space - where n is the length of the input string.
def reverseWordsInString(string):
    if len(string) < 1:
        return ""

    reversedArray = []
    # the pair of pointers are initialized at the starting index.
    start = 0
    end = 0
    # So long as the end pointer is still in bound, continue the loop.
    while end <= len(string) - 1:
        if not isTimeToSlice(start, end, string):
            # when it is not at the position to slice, keep extending the end
            # pointer by one position at a time
            if end == len(string) - 1:
                # if we have reached the last index of the array, insert the
                # substring so far to the result.
                reversedArray.insert(0, string[start:end + 1])
            end += 1
        else:
            # slice the array by taking the subarray from start pointer the the
            # index before end poiner, and add it to beginning of the result
            # array.
            reversedArray.insert(0, string[start:end])
            print(reversedArray)
            # shift start to end
            start = end
    return "".join(reversedArray)

# This is a helper function that determines whether we should slice the string.
def isTimeToSlice(start, end, string):
    # it is the position where it is a single space or the last space in a row
    # of spaces, and the next character is the first letter of a word.
    spaceToWord = (string[start] == " " and string[end] != " ")
    # it is the position where it is the last letter of a word, and the next
    # position is a space.
    wordToSpace = (string[start] != " " and string[end] == " ")
    return spaceToWord or wordToSpace
