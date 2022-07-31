# Notes:
# This is the naive solution, it works but the time complexity is not very good.
# For each smallStrings, we essentially iterate through each letters in the
# bigString, and determine whether there is a match for the smallString.
#
# Complexity:
# O(bns) time | O(n) space - where n is the number of the small
# strings, s is the length of the longest small string, and b is the length of
# the big string.
def multiStringSearch(bigString, smallStrings):
    return [isInBigString(bigString, smallString) for smallString in smallStrings]

def isInBigString(bigString, smallString):
    for i in range(len(bigString)):
        if i + len(smallString) > len(bigString):
            break
        if isInBigStringHelper(bigString, smallString, i):
            return True
    return False

def isInBigStringHelper(bigString, smallString, startIdx):
    leftBigIdx = startIdx
    rightBigIdx = startIdx + len(smallString) - 1
    leftSmallIdx = 0
    rightSmallIdx = len(smallString) - 1
    while leftBigIdx <= rightBigIdx:
        if bigString[leftBigIdx] != smallString[leftSmallIdx] or bigString[rightBigIdx] != smallString[rightSmallIdx]:
            return False
        leftBigIdx += 1
        rightBigIdx -= 1
        leftSmallIdx += 1
        rightSmallIdx -= 1
    return True

# The standard solution uses the Suffix Trie data structure to store the
# big string, and iterate through the small strings to see if the small string
# is contained in the Suffix Trie.
#
# If a small string is contained in the Suffix Trie we built based on the big
# string, it means it is contained in the big string. Note that the suffix Trie
# here does not need any end symbol.
#
# Complexity:
# O(n^2 + ns) time | O(b^2 + n) space - where n is the number of the small
# strings, s is the length of the longest small string, and b is the length of
# the big string.
def multiStringSearch(bigString, smallStrings):
    modifiedSuffixTrie = ModifiedSuffixTrie(bigString)
    return [modifiedSuffixTrie.contains(string) for string in smallStrings]

class ModifiedSuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.populateModifiedSuffixTrieFrom(string)

    # the function that calls the untility function which inserts the suffixes
    # of the string to build the Suffix Trie
    def populateModifiedSuffixTrieFrom(self, string):
        for i in range(len(string)):
            self.insertSubstringStartingAt(i, string)

    # the utility function which actually inserts the suffix strating at the i
    # index of the orginal string to the Trie
    def insertSubstringStartingAt(self, i ,string):
        node = self.root
        for j in range(i, len(string)):
            letter = string[j]
            if letter not in node:
                node[letter] = {}
            node = node[letter]

    # the utility function which checks if a given string is contained in the
    # Suffix Trie
    def contains(self, string):
        node = self.root
        for letter in string:
            if letter not in node:
                return False
            node = node[letter]
        return True

# The optimal solution also uses a Trie data structure, but it is used to store
# each of the small strings, and we do use the end symbol this time.
#
# We iterate through the letters of the big string, for each letter, we now
# check which small strings are contained in the rest of the big string starting
# at that letter(a suffix).
#
# Complexity:
# O(ns + bs) time | O(ns) - where n is the number of the small
# strings, s is the length of the longest small string, and b is the length of
# the big string.
class Trie:
    def __init__(self):
        self.root = {}
        self.endSymbol = "*"

    # build the Trie based on the given string
    def insert(self, string):
        # starting at the root node
        current = self.root
        # iterate each letters of the string
        for i in range(len(string)):
            # if the letter is not in the node hash table already, create an
            # empty node/hash table
            if string[i] not in current:
                current[string[i]] = {}
            # jump to the node/hash table
            current = current[string[i]]
        # always add the end symbol to the node to indicate the string is
        # complete
        current[self.endSymbol] = string

def multiStringSearch(bigString, smallStrings):
    # initialize the Trie data structure, and fill it with the small strings
    trie = Trie()
    for string in smallStrings:
        trie.insert(string)
    # use a hash table to track the small strings found by traversing the
    # the big string
    containedStrings = {}
    for i in range(len(bigString)):
        findSmallStringsIn(bigString, i, trie, containedStrings)
    return [string in containedStrings for string in smallStrings]

def findSmallStringsIn(string, startIdx, trie, containedStrings):
    currentNode = trie.root
    for i in range(startIdx, len(string)):
        currentChar = string[i]
        if currentChar not in currentNode:
            break
        currentNode = currentNode[currentChar]
        if trie.endSymbol in currentNode:
            containedStrings[currentNode[trie.endSymbol]] = True
