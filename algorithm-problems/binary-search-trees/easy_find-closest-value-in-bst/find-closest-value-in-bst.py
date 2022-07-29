# Notes:
# We can solve this problem using the iterative approach.
# By the setup of BST, any left node is strictly smaller than its parent, and
# the right node is greater than or equal to the parent.
#
# We start at the root node and compare the current node with the target value
# by taking the absolute value of the difference, we keep track of the closest
# value, and keep traverse down to the left or right child depending on whether
# the current node is smaller or greater than the target. If the current node is
# equal to the target, we are done.
#
# Complexity:
# Average - O(log(n)) time | O(1) space - where n is the number of nodes.
# Worst   - O(n) time | O(1) space
def findClosestValueInBst(tree, target):
    return findClosestValueInBstHelper(tree, target, tree.value)

def findClosestValueInBstHelper(tree, target, closest):
    currentNode = tree
    while currentNode is not None:
        if abs(target - closest) > abs(target - currentNode.value):
            closest = currentNode.value
        if target < currentNode.value:
            currentNode = currentNode.left
        elif target > currentNode.value:
            currentNode = currentNode.right
        else:
            break
    return closest

# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
