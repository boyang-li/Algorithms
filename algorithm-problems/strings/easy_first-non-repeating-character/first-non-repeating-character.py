# Brute-force approach: having two pointers at the begingning index,
# and start a double nested loop. try to find the first non duplicating
# character by shifting the pointers.
#
# O(n^2) time | O(1) time - where n is the legnth of the input string
def firstNonRepeatingCharacter(string):
    for i in range(len(string)):
        foundDup = False
        for j in range(len(string)):
            if string[i] == string[j] and i != j:
                foundDup = True

        if not foundDup:
            return i
    return -1

# Optimal solution: use an auxiliary data structure to keep
# the frequencies of each characters in the string.
#
# O(n) time | O(1) time - where n is the legnth of the input string
# the constant space is because the input string only has lowercase
# English-alphabet letters; thus, out hash table will never have more
# than 26 characters frequencies and that is equivalent to constant
# space in the big-O notaiton.
def firstNonRepeatingCharacter(string):
    charFreq = {}
    for char in string:
        charFreq[char] = charFreq.get(char, 0) + 1

    for i in range(len(string)):
        char = string[i]
        if charFreq[char] == 1:
            return i
    return -1
