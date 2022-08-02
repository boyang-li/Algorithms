# Notes:
# To solve this problem, we use a Trie data structure to store the target words,
# and then traverse the board in the DFS fashion to explored matching letters
# for each words.
#
# At any element in the board, we explore its neighbors for the next matching
# letter, and use a 'visited' matrix for sanity check to avoid repeated letter.
#
# Unlike a regular Trie, the end symbol is just an empty node, we atually store
# the word as the value of the end symbol, so that we could easily store the
# word to the output once we have found it in the board.
#
# Complexity:
# the traversal of the board woulr run in O(nm) time, the neighbor exploring
# for each element would be O(8^s) time, and s would be the length of the
# longest word. Insering the letters into the Trie for each words would be
# O(ws) time. For auxiliary data structure, storing the 'visited' matrix would
# take O(nm) space, and storing the Trie would be O(ws).
#
# O(nm*8^s + ws) time | O(nm + ws) space - where n is the height of the board, m
# is the height of the board, w is the number of the words, and s is the length
# of the longest word.
def boggleBoard(board, words):
    trie = Trie()
    for word in words:
        trie.add(word)
    finalWords = {}
    visited = [[False for letter in row] for row in board]
    for i in range(len(board)):
        for j in range(len(board[i])):
            explore(i, j, board, trie.root, visited, finalWords)
    return list(finalWords.keys())

def explore(i, j, board, trieNode, visited, finalWords):
    if visited[i][j]:
        return
    letter = board[i][j]
    if letter not in trieNode:
        return
    visited[i][j] = True
    trieNode = trieNode[letter]
    if "*" in trieNode:
        finalWords[trieNode["*"]] = True
    neighbors = getNeighbors(i, j, board)
    for neighbor in neighbors:
        explore(neighbor[0], neighbor[1], board, trieNode, visited, finalWords)
    visited[i][j] = False

# explore the neighbors of the element located at [i, j] in the matrix in
# clock-wise order.
def getNeighbors(i, j, board):
    neighbors = []

    # if not on the top border, check top neighbor.
    if i > 0:
        neighbors.append([i - 1, j])
    # if not at the top-right corner, check diagonally top-right neighbor.
    if i > 0 and j < len(board[0]) - 1:
        neighbors.append([i - 1, j + 1])
    # if not at the right border, check the right neighbor.
    if j < len(board[0]) - 1:
        neighbors.append([i, j + 1])
    # if not at the bot-right corner, check the bot-right neighbor.
    if i < len(board) - 1 and j < len(board[0]) - 1:
        neighbors.append([i + 1, j + 1])
    # if not at the bottom border, check the bottom neighbor.
    if i < len(board) - 1:
        neighbors.append([i + 1, j])
    # if not at the bot-left corner, check the bot-left neighbor.
    if i < len(board) - 1 and j > 0:
        neighbors.append([i + 1, j - 1])
    # if not at the left border, check the left neighbor.
    if j > 0:
        neighbors.append([i, j - 1])
    # if not at the top-left corner, check the top-left neighbor.
    if i > 0 and j > 0:
        neighbors.append([i - 1, j - 1])
    return neighbors

class Trie:
    def __init__(self):
        self.root = {}
        self.endSymbol = "*"

    # for a given string, add each letter to the Trie strating from
    # the root node
    def add(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.endSymbol] = word
