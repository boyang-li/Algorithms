# LeetCode 680. Valid Palindrome II
#
# Notes:
# This is very silimar to the Valid Palindrome problem, but we are allowed to
# have at most 1 mismatch as we validate the string. Upon the first time that we
# detect a mismatch, we can ignore the elements we have already compared.
# We can validate the substring one more time for each of the following inputs:
# the rest of the string with left incremented by 1, and the rest of the string
# with right decremented by 1. If either of the validations shows a valid
# palindrome, the original string is still considered "valid palindome".
#
# Complexity:
# O(n) time | O(1) space - where n is the length of the string.

# My solution
# not quite correct--it breaks when the input string is a palindrome with even
# number of letters, but is also palindromic after removing a letter.
# i.e. "bddb", removing 'd' becomes "bdb" and its still a palindrome.
def validPalindromeAttempt(s: str) -> bool:
    if len(s) == 0:
        return False
    elif len(s) == 1:
        return True

    left, right = 0, len(s) - 1
    mismatch = 0
    while left < right:
        # print("left=", left, " leftVal=", s[left], " right=", right, " rightVal=", s[right], " mismatch=", mismatch)
        if mismatch > 2:
            return False

        if s[left] == s[right]:
            left += 1
            right -= 1
            continue
        elif mismatch == 0:
            # first attempt shift left and hold right still
            left += 1
        elif mismatch == 1:
            # this is the second time we see a mismatch, this time we put left back
            # and shift right
            left -= 1
            right -= 1

        mismatch += 1

    # print("len(s) mode 2=", len(s) % 2)
    if (len(s) % 2 == 0) and mismatch == 0:
        return False
    return True

def validPalindrome(s: str) -> bool:
    def check_palindrome(s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True

    left = 0
    right = len(s) - 1
    while left < right:
        # Found a mismatched pair - try both deletions
        if s[left] != s[right]:
            return check_palindrome(s, left, right - 1) or check_palindrome(s, left + 1, right)
        left += 1
        right -= 1

    return True

def main():
    print(validPalindrome("abccbxa")) # True
    print(validPalindrome("bddb")) # True
    print(validPalindrome("bddbfff")) # False

if __name__ == "__main__":
  main()
