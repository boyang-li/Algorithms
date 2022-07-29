# Notes:
# Recall that the InOrder, PreOrder, and PostOrder are recursive traversal
# functions defined as the following:
# - InOrder: traverse the left child recursively, record the current node value,
# and then traverse the right child recursively.
#
# - PreOrder: record the current node value, traverse the left child recursively
# and then traverse the right child recursively.
#
# - PostOrder: traverse the left child recursively, traverse the right child
# recursively, and then record the current node value.
#
# Stop the traversal when the current node is None.
#
# Complexity:
# We are going to visit every node in the BT, and there could be at most n
# recursive calls on the memory stack.
# O(n) time | O(n) space - where n is the number of nodes in the BT.
def inOrderTraverse(tree, array):
  if tree is not None:
    inOrderTraverse(tree.left, array)
    array.append(tree.value)
    inOrderTraverse(tree.right, array)
  return array

# O(n) time | O(n) space
def preOrderTraverse(tree, array):
  if tree is not None:
    array.append(tree.value)
    preOrderTraverse(tree.left, array)
    preOrderTraverse(tree.right, array)
  return array

# O(n) time | O(n) space
def postOrderTraverse(tree, array):
  if tree is not None:
    postOrderTraverse(tree.left, array)
    postOrderTraverse(tree.right, array)
    array.append(tree.value)
  return array
