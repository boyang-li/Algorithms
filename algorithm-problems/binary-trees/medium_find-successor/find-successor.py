# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

## Naive solution
# O(n) time | O(n) space - where n is the number of nodes in the tree
def findSuccessor(tree, node):
    inOrderTraversalOrder = getInOrderTraversalOrder(tree)

    for idx, currNode in enumerate(inOrderTraversalOrder):
        if currNode != node:
            continue

        if idx == len(inOrderTraversalOrder) - 1:
            return None

        return inOrderTraversalOrder[idx + 1]

def getInOrderTraversalOrder(node, order=[]):
    if node is None:
        return order

    getInOrderTraversalOrder(node.left, order)
    order.append(node)
    getInOrderTraversalOrder(node.right, order)

    return order

## Optimal solution
# O(h) time | O(1) space - where h is the height of the tree
def findSuccessor(tree, node):
    if node.right is not None:
        return getLeftmostChild(node.right)

    return getRightmostParent(node)

def getLeftmostChild(node):
    currNode = node
    while currNode.left is not None:
        currNode = currNode.left

    return currNode

def getRightmostParent(node):
    currNode = node
    while currNode.parent is not None and currNode.parent.right == currNode:
        currNode = currNode.parent

    return currNode.parent
