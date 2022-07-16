# O(n) time | O(n) space - where n is the length of the array 
def minHeightBst(array):
  return minHeightBstHelper(array, 0, len(array) - 1)

def minHeightBstHelper(array, leftIdx, rightIdx):
  if leftIdx < 0 or rightIdx > len(array) - 1 or leftIdx > rightIdx:
    return None

  parentIdx = (leftIdx + rightIdx)//2
  parentNode = BST(array[parentIdx])
  parentNode.left = minHeightBstHelper(array, leftIdx, parentIdx - 1)
  parentNode.right = minHeightBstHelper(array, parentIdx + 1, rightIdx)
  return parentNode

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
