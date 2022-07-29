# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Notes:
# We can solve it using the recusive approach, we know for a fact that for each
# node in a valid BST, every node is strictly smaller than it to the left, and
# every node is greater than or equal to it to the right. So we simply set
# the current node's value as the max/min bound and recursively check whether
# both child nodes are valid BST nodes.
#
# Complexity:
# O(n) time | O(d) space, where n is the number of nodes in the tree,
# and d is the depth(height) of the tree.
def validateBst(tree):
    return validateBstHelper(tree, float("-inf"), float("inf"))

def validateBstHelper(tree, min, max):
    if tree is None:
        return True
    if tree.value < min or tree.value >= max:
        return False
    leftValid = validateBstHelper(tree.left, min, tree.value)
    return leftValid and validateBstHelper(tree.right, tree.value, max)
