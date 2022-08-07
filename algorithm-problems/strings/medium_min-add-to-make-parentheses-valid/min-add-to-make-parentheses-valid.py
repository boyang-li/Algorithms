# Notes:
# use a counter to track '('s, and whenever we see a ')', decrement 1
# from the counter. If the counter is 0, we are in short of '(', it means
# a '(' needed to be inserted in order to make the string valid. However,
# we do not need to actually insert it, we just need the minimum number
# of '('s we need to add, so use another counter for it.
#
# Complexity:
# O(n) time | O(1) space - where n is the length of the string.
def minAddToMakeValid(s: str) -> int:
    if not s or s == '':
        return True


    outstandingOpenParens, missingCloseParens = 0, 0

    for i in range(len(s)):
        if s[i] == '(':
            outstandingOpenParens += 1
        elif s[i] == ')':
            if outstandingOpenParens > 0:
                outstandingOpenParens -= 1
            else:
                missingCloseParens += 1

    if outstandingOpenParens > 0:
        return outstandingOpenParens + missingCloseParens
    return missingCloseParens
