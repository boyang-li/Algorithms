# Do not edit the class below except for the
# populateSuffixTrieFrom and contains methods.
# Feel free to add new properties and methods
# to the class.
class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    # this function allows us to build out a suffix trie
    # of the characters in the string
    # O(nˆ2) time | O(nˆ2) space
    def populateSuffixTrieFrom(self, string):
        for i in range(len(string)):
            self.insertSubstringStartingAt(i, string)

    # given a starting index of a character of string,
    # insert the character and the rest characters of the
    # string to the suffix trie
    def insertSubstringStartingAt(self, i, string):
        node = self.root
        for j in range(i, len(string)):
            letter = string[j]
            # if the letter is not found in the current node,
            # don't insert it just yet, create a new node for it.
            if letter not in node:
                node[letter] = {}
            # wheter the letter is found or not, go to that node
            node = node[letter]
        # at the end of the string, always add the end symbol
        node[self.endSymbol] = True

    # O(m) time | O(1) space
    def contains(self, string):
        node = self.root
        for letter in string:
            if letter not in node:
                return False
            node = node[letter]
        return self.endSymbol in node
