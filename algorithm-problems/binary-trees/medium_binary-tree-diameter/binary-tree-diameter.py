class BianryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class TreeInfo:
    def __init__(self, diameter, height):
        self.diameter = diameter
        self.height = height

# Average case: when the tree is balanced
# O(n) time | O(h) space - where n is the number of nodes in the
# binary tree and h is the height of the binary tree
def binaryTreeDiameter(tree):
    return getTreeInfo(tree).diameter

def getTreeInfo(tree):
    if tree is None:
        return TreeInfo(0, 0)

    leftTreeInfo = getTreeInfo(tree.left)
    rightTreeInfo = getTreeInfo(tree.right)

    longestPathThroughRoot = leftTreeInfo.height + rightTreeInfo.height
    maxDiameterSoFar = max(leftTreeInfo.diameter, rightTreeInfo.diameter)
    currDiameter = max(longestPathThroughRoot, maxDiameterSoFar)
    currHeight = max(leftTreeInfo.height, rightTreeInfo.height) + 1

    return TreeInfo(currDiameter, currHeight)
