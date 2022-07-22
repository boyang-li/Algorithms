# O(n) time | O(min(n, a)) - where n is the length of the string,
# and a is the maximum number of unique characters in the substring.
def longestSubstringWithoutDuplication(string):
    # use a hash table to store the indices of characters we have seen
    lastSeen = {}
    # use a pair of poniters to represent the output substring
    longest = [0, 1]
    startIdx = 0
    for i, char in enumerate(string):
        if char in lastSeen:
            # we have found a dup, now shift the start index
            # to the appropriate position - the larger index
            # between startIdx and the one next to the duplicate.
            startIdx = max(startIdx, lastSeen[char] + 1)

        if longest[1] - longest[0] < i + 1 - startIdx:
            # now if the current substring is greater than
            # the longest on record, update longest
            longest = [startIdx, i + 1]
        lastSeen[char] = i

    return string[longest[0]:longest[1]]
