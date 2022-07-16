# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# The brute-force solution to this problem. We can build a 
# sorted array for all the values in the BST, and then find
# the kth largest value in the sorted array.
#
# O(n) time | O(n) space - where n is the number of nodes in the BST
def findKthLargestValueInBst(tree, k):
    sortedNodeValues = []
    inOrderTraverse(tree, sortedNodeValues)
    return sortedNodeValues[len(sortedNodeValues) - k]

def inOrderTraverse(node, sortedNodeValues):
    if node == None:
        return

    inOrderTraverse(node.left, sortedNodeValues)
    sortedNodeValues.append(node.value)
    inOrderTraverse(node.right, sortedNodeValues)

# The optimal solution to this problem. We can build a 
# sorted array for all the values in the BST, and then find
# the kth largest value in the sorted array.
class TreeInfo:
  def __init__(self, nodesVisited, lastNodeValue):
    self.nodesVisited = nodesVisited
    self.lastNodeValue = lastNodeValue

# O(h + k) time | O(h) space - where h is the height of the BST and k is the
# input param. Notice that it takes O(h) to traverse to the largest node in
# the BST, and from there, it takes O(k) to find the kth largest node.
#
# For space complexity, there are at most h un-processed recursive calls
# in the memory stack, hence O(h) space.
def findKthLargestValueInBst(tree, k):
  treeInfo = TreeInfo(0, -1)
  reverseInorderTraverse(tree, k, treeInfo)
  return treeInfo.lastNodeValue

def reverseInorderTraverse(node, k, treeInfo):
  if node is None or treeInfo.nodesVisited >= k:
    return

  # go the the right child node
  reverseInorderTraverse(node.right, k, treeInfo)
  # if we have not reached kth node, update values and go to the left child
  if treeInfo.nodesVisited < k:
    treeInfo.nodesVisited += 1
    treeInfo.lastNodeValue = node.value
    reverseInorderTraverse(node.left, k, treeInfo)
