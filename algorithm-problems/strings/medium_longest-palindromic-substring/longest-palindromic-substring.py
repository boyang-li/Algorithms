# Notes:
# We solve this problem by construction a double nested loop. We iterate through
# the input array with a pair of pinters, left and right, initialy set up
# back-to-back in the beginning of each iteration, then gradually extend to
# both directions to find the longest palindromic substring.
#
# Note that the inner loop needed to be called twice, once for odd length and
# once for even length of substring. We keep track of the longest palindromic
# substring among all.
#
# Complexity:
# O(nˆ2) time | O(n) space - where n is the length of the string
def longestPalindromicSubstring(string):
    # the initial pair of pointers are set up back-to-back, where the left
    # pointer located at the starting index of the input array.
    currentLongest = [0, 1]
    for i in range(1, len(string)):
        # call the inner loop for odd length of substring, where the value at
        # the center does not need to be compared.
        odd = getLongestPalindromeFrom(string, i - 1, i + 1)
        # call the inner loop for even length of substring, where every value
        # needed to be checked for palindrome.
        even = getLongestPalindromeFrom(string, i - 1, i)
        # get the longer palindomic substring between the results of the odd and
        # even calls.
        longest = max(odd, even, key=lambda x: x[1] - x[0])
        # keep track of the longest palindromic substring so far.
        currentLongest = max(longest, currentLongest, key=lambda x: x[1] - x[0])
    return string[currentLongest[0] : currentLongest[1]]

def getLongestPalindromeFrom(string, leftIdx, rightIdx):
    # So long as the left and right pointers are still in bounds, continue
    # extending.
    while leftIdx >= 0 and rightIdx < len(string):
        if string[leftIdx] != string[rightIdx]:
            break
        leftIdx -= 1
        rightIdx += 1
    # the real right index would be (rightIdx - 1), here we are dealing with
    # the string slicing exclusive ending index issue by not subtracting 1.
    return [leftIdx + 1, rightIdx]
