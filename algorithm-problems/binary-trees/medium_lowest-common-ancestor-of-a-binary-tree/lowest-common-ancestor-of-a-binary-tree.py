# LeetCode 236. Lowest Common Ancestor of a Binary Tree
#
# Notes:
# There are multiple approaches to solve this problem: recursion, iteration
# using parent pointers and iteration without parent pointers. We have covered
# the recursive approach in below.
#
# Complexity:
# O(n) time | O(n) space - where n is the number of nodes it the binary tree.
# note that the space complexity is O(d) where d it the height of the BT, but in
# the worst case d = n, thus we write O(n) space.
def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    return getTreeInfo(root, p, q).lca

def getTreeInfo(root, nodeOne, nodeTwo):
    targetNodesFound = 0

    children = [root.left, root.right]
    for child in children:
        if child is None:
            continue

        treeInfo = getTreeInfo(child, nodeOne, nodeTwo)

        if treeInfo.lca is not None:
            return treeInfo

        targetNodesFound += treeInfo.targetNodesFound

    if root == nodeOne or root == nodeTwo:
        targetNodesFound += 1

    lca = root if targetNodesFound == 2 else None
    return TreeInfo(lca, targetNodesFound)

class TreeInfo:
    def __init__(self, lca, targetNodesFound):
        self.lca = lca
        self.targetNodesFound = targetNodesFound

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
