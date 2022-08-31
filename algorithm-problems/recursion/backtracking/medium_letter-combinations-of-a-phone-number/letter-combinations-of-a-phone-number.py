# LeetCode 17. Letter Combinations of a Phone Number
#
# Notes:
# Solve this using a standard backtracking algorithm template. Let's break down
# the problem, by starting with an input that is only 1-digit long, for example
# digits = "2". This example is trivial - just generate all letters that
# correspond with digit = "2", which would be ["a", "b", "c"].
#
# What if instead we had a 2-digit long input, digits = "23"? Imagine taking
# each letter of digit = "2" as a starting point. That is, lock the first letter
# in, and solve all the possible combinations that start with that letter. If
# our first letter will always be "a", then the problem is trivial again - it's
# the 1-digit case, and all we have to do is generate all the letters
# corresponding with digit = "3", and add that to "a", to get ["ad", "ae","af"].
# This was easy because we ignored the first letter, and said it will always be
# "a". But we know how to generate all the first letters too - it's the 1-digit
# case which we already solved to be ["a", "b", "c"].
#
# As you can see, solving the 1-digit case is trivial, and solving the 2-digit
# case is just solving the 1-digit case twice. The same reasoning can be
# extended to n digits.
#
# Complexity:
# O(4^n * n) time | O(n) space - where N is the length of digits. Note that 4 in
# this expression is referring to the maximum value length in the hash map, and
# not to the length of the input. The worst-case is where the input consists of
# only 7s and 9s. In that case, we have to explore 4 additional paths for every
# extra digit. Then, for each combination, it costs up to N to build the
# combination. This problem can be generalized to a scenario where numbers
# correspond with up to M digits, in which case the time complexity would be
# O(M^N * N) time. For the problem constraints, we're given, M = 4, because of
# digits 7 and 9 having 4 letters each.

from typing import List

def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
                  "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        def backtrack(index, path):
            # if the path is the same length as digits, we have a complete combination
            if len(path) == len(digits):
                combinations.append("".join(path))
                return # backtrack

            # get the letters that the current digit maps to, and loop through them
            possibleLetters = letters[digits[index]]
            for letter in possibleLetters:
                # add the letter to our current path
                path.append(letter)
                # move on to the next digit
                backtrack(index + 1, path)
                # backtrack by removing the letter begore moving onto the next
                path.pop()

        # initiate backtracking with an empty path and starting index of 0
        combinations = []
        backtrack(0, [])
        return combinations
