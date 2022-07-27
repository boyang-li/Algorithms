# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# O(n) time | O(n) space - where n is the number of nodes in the tree
def findNodesDistanceK(tree, target, k):
    nodesToParents = {}
    populateNodesToParents(tree, nodesToParents)
    targetNode = getNodeFromValue(target, tree, nodesToParents)

    return bfsFromNodesDistanceK(targetNode, nodesToParents, k)

def bfsFromNodesDistanceK(targetNode, nodesToParents, k):
    queue = [(targetNode, 0)]
    seen = {targetNode.value}
    while len(queue) > 0:
        currentNode, distanceFromTarget = queue.pop(0)
        if distanceFromTarget == k:
            nodesDistanceK = [node.value for node, _ in queue]
            nodesDistanceK.append(currentNode.value)
            return nodesDistanceK

        connectedNodes = [currentNode.left, currentNode.right, nodesToParents[currentNode.value]]
        for node in connectedNodes:
            if node is None:
                continue

            if node.value in seen:
                continue

            seen.add(node.value)
            queue.append((node, distanceFromTarget + 1))

    return []

def populateNodesToParents(node, nodesToParents, parent=None):
   if node is not None:
       nodesToParents[node.value] = parent
       populateNodesToParents(node.left, nodesToParents, node)
       populateNodesToParents(node.right, nodesToParents, node)

def getNodeFromValue(value, tree, nodesToParents):
    if tree.value == value:
        return tree

    nodeParent = nodesToParents[value]
    if nodeParent.left is not None and nodeParent.left.value == value:
        return nodeParent.left

    return nodeParent.right
