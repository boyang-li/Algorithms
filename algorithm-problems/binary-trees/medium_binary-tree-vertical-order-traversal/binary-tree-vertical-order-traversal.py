# LeetCode 314. Binary Tree Vertical Order Traversal
#
# Notes:
# This is yet another problem about Binary Tree traversals. As one would
# probably know, the common strategies to traverse a Tree data structure are
# Breadth-First Search (a.k.a BFS) and Depth-First Search (a.k.a. DFS).
#
# The DFS strategy can be further distinguished as preorder DFS, inorder DFS and
# postorder DFS, depending on the relative order of visit among the node itself
# and its child nodes.
#
# In the problem description, we are asked to return the vertical order of a
# binary tree, which actually implies two sub-orders, where each node would have
# a 2-dimensional index (denoted as <column, row>)
#
# we can now formulate the problem as a task to order the nodes based on the
# 2-dimensional coordinates that we defined above. More specifically, the nodes
# should be ordered by column first, and further the nodes on the same column
# should be ordered vertically based on their row indices.
class Solution:

    # Approach 1: Breadth-First Search (BFS)
    # O(nlog(n)) time | O(n) space

    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # use a hash table to store node value with column index as keys.
        columnTable = defaultdict(list)

        # use queue for BFS traversal, save both the node and its cloumn index in
        # a tuple.
        queue = deque([(root, 0)])

        while queue:
            # consume an element from the queue.
            node, column = queue.popleft()

            # populate the hash table, the node will be row-wise ordered since
            # we used BFS traversal.
            columnTable[column].append(node.val)

            if node.left: # push the left child node to the queue if it exists
                queue.append((node.left, column - 1))
            if node.right: # push the reight child node to the queue if it exists
                queue.append((node.right, column + 1))

        # we order the hash table by keys/column indexes, so the output nested list
        # is column-wise ordered.
        return [columnTable[x] for x in sorted(columnTable.keys())]

    # Approach 2: BFS *Without Sorting*
    # O(n) time | O(n) space

    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        columnTable = defaultdict(list)
        queue = deque([(root, 0)])
        # Realise that we can use a range to generate column indexes in order
        # if we know the max/min columns
        min_column = max_column = 0

        while queue:
            node, column = queue.popleft()

            columnTable[column].append(node.val)

            # update the min/max columns
            min_column = min(min_column, column)
            max_column = max(max_column, column)

            if node.left: # push the left child node to the queue if it exists
                queue.append((node.left, column - 1))
            if node.right: # push the reight child node to the queue if it exists
                queue.append((node.right, column + 1))

        return [columnTable[x] for x in range(min_column, max_column + 1)]

    # Approach 3: Depth-First Search (DFS)
    #
    # Complexity:
    # O(w * h * log(h)) time | O(n) - where w is the width of the BT, and h is
    # the height of the BT.
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        columnTable = defaultdict(list)
        min_column = max_column = 0

        def DFS(node, row, column):
            if node is not None:
                nonlocal min_column, max_column
                columnTable[column].append((row, node.val))
                min_column = min(min_column, column)
                max_column = max(max_column, column)

                # preorder DFS
                DFS(node.left, row + 1, column - 1)
                DFS(node.right, row + 1, column + 1)

        DFS(root, 0, 0)

        # order by column and sort by row
        ret = []
        for col in range(min_column, max_column + 1):
            columnTable[col].sort(key=lambda x:x[0])
            colVals = [val for row, val in columnTable[col]]
            ret.append(colVals)

        return ret

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
