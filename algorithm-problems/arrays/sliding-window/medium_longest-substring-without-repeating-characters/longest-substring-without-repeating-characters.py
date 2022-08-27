# LeetCode 3. Longest Substring Without Repeating Characters
#
# Notes:
# we use two pointers to construct a 'sliding window', the right pointer
# is used to 'extend' the window, and the left pointer is used to 'contract' the
# window. In addition, we use a hash table to store the index of the character
# that we have seen.
#
# Complexity:
# O(n) time | O(min(m, n)) space, where n is the length of the input string and
# m is the size of the charset/alphabet.
#
# We need O(k)O(k) space for checking a substring has no duplicate characters,
# where kk is the size of the Set. The size of the Set is upper bounded by the
# size of the string nn and the size of the charset/alphabet m.
def lengthOfLongestSubstring(s: str) -> int:
    n = len(s)

    left = 0
    dupIndexes = {}
    maxSubstrLen = 0

    for right in range(n):
        if s[right] in dupIndexes:
            left = max(dupIndexes[s[right]], left)

        maxSubstrLen = max(right - left + 1, maxSubstrLen)
        # we save the next index to the right pointer, so the new left will
        # start at it.
        dupIndexes[s[right]] = right + 1

    return maxSubstrLen
