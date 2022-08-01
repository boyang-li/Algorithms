# Notes:
# We are solving this problem using a hash table which stores the letters we
# have seen, and maintain a pointer indicating the start position of a substring
# without duplicate in each iterations as we traverse the input string. We keep
# track of the interval of the longest non-dup substring as we iterate.
#
# Complexity:
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

        # so long as the substring starting from the startIdx up until the
        # current index, we extend the substring as i gets incremented and
        # keep track of the longest non-dup substring as an interval of
        # startIdx and i + 1(we use this for string slicing so it is exclusive).
        if longest[1] - longest[0] < i + 1 - startIdx:
            # now if the current substring is greater than the longest so far,
            # update the interval.
            longest = [startIdx, i + 1]
        # do not forget to update lastSeen hash table at the end.
        lastSeen[char] = i

    return string[longest[0]:longest[1]]
