# LeetCode 1650. Lowest Common Ancestor of a Binary Tree III
#
# Notes:
# This is the classic LCA type problem. In this problem, we are given the
# access to the parent node, so we can backtrack to the root node from node p
# and q to get the depth. Then we want to backtrack the lower node to bring it
# to the same level as the other node, and backtrack them at the same time until
# they reach the LCA.
#
# Complexity:
# O(n) time | O(d) space - n is the number of nodes in the tree, and d is the
# depth/height of the tree. note that in the worst case, d = n.
"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        def backtrack(node, levelsToGo):
            while node.parent and levelsToGo > 0:
                node = node.parent
                levelsToGo -= 1
            return node

        def getDepth(node):
            depth = 1
            while node.parent:
                node = node.parent
                depth += 1
            return depth

        # get the depth of p and q
        depthP = getDepth(p)
        depthQ = getDepth(q)
        print("depthP=", depthP, " depthQ=", depthQ)

        # backtrack the lower node of p and q until both nodes are at the same level
        if depthP > depthQ:
            # backtrack q
            p = backtrack(p, depthP - depthQ)
        elif depthP < depthQ:
            # backtrack P
            q = backtrack(q, depthQ - depthP)

        print("P=", p.val, " Q=", q.val)

        # backtrack p and q at the same time until we find the LCA
        while p.val != q.val:
            q = backtrack(q, 1)
            p = backtrack(p, 1)

        return p
