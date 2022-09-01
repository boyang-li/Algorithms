# LeetCode 101. Symmetric Tree
#
# Notes:
# A tree is symmetric if the left subtree is a mirror reflection of the right
# subtree. Therefore, the question is: when are two trees a mirror reflection
# of each other?
# Two trees are a mirror reflection of each other if:
#   1. Their two roots have the same value.
#   2. The right subtree of each tree is a mirror reflection of the left subtree
#      of the other tree, and vice versa.
#
# Complexity:
# O(n) time | O(n) space
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isMirror(node1, node2):
    if (node1 == None and node2 == None):
        return True

    if (node1 == None or node2 == None):
        return False

    return node1.val == node2.val and isMirror(node1.right, node2.left) and isMirror(node1.left,node2.right)

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return isMirror(root, root)
