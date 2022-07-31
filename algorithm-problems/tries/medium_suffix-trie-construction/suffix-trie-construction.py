# Notes:
# The Suffix Trie is a simpler data structure which is very much like a tree.
# It is built based on a string, and contains all the suffixes of the string.
#
# The suffixes start from the same letters which are already stored in the tree,
# and are ended with a asterik.
#
# Complexity:
# Build - O(n^2) time | O(n^2) space, where n is the number of letters in the
# input string.
# Search - O(m) time | O(1) space, where m is the length of the string we are
# searching for.
class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    # this function builds the suffix trie based on the character of the string.
    # O(nˆ2) time | O(nˆ2) space
    def populateSuffixTrieFrom(self, string):
        for i in range(len(string)):
            self.insertSubstringStartingAt(i, string)

    # given the starting index of a character in the string, insert all of the
    # characters to the suffix trie.
    def insertSubstringStartingAt(self, i, string):
        node = self.root
        # for each characters from the ith index to the end of the input string
        for j in range(i, len(string)):
            letter = string[j]
            # if the letter is not found in the current node, create a new node.
            # a node is basically a hash table, and it gives us constant time
            # for character lookup.
            if letter not in node:
                node[letter] = {}
            # jump to the new node
            node = node[letter]
        # at the end of the string, always add the end symbol
        node[self.endSymbol] = True

    # this would be the Search operation of the Suffix Trie
    # O(m) time | O(1) space
    def contains(self, string):
        node = self.root
        for letter in string:
            if letter not in node:
                return False
            node = node[letter]
        return self.endSymbol in node
