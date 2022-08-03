# Notes:
# To solve this question, we treat it as a graph problem, and the graph is in
# tree structure where we start at the descendant nodes and can only go upward.
#
# Realise that we want to first bring the two descendant nodes at the same
# depth, backtrack both of them at the same pace, and then we will eventually
# get the lowest common ancestor.
#
# Complexity:
# We can solve this problem with iterative approach.
# O(d) time | O(1) space - where d is the deepest descendant in the graph.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None

def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    depthOne = getDescendantDepth(descendantOne, topAncestor)
    depthTwo = getDescendantDepth(descendantTwo, topAncestor)

    # keep backtracking until we have found the lowest common ancestor.
    if depthOne > depthTwo:
        return backtrackAncestralTree(descendantOne, descendantTwo, depthOne - depthTwo)
    else:
        return backtrackAncestralTree(descendantTwo, descendantOne, depthTwo - depthOne)

# This function returns the depth of the descendant
def getDescendantDepth(descendant, topAncestor):
    depth = 0
    while descendant != topAncestor:
        depth += 1
        descendant = descendant.ancestor
    return depth

# This function takes two descendants and backtrack them at the same pace.
def backtrackAncestralTree(lowerDescendant, higherDescendant, diff):
    # when evern the depth of the two descendants are different, switch them
    # around to balance the difference.
    while diff > 0:
        lowerDescendant = lowerDescendant.ancestor
        diff -= 1
    # keep updating the lower/higher descendant until they are the same node.
    while lowerDescendant != higherDescendant:
        lowerDescendant = lowerDescendant.ancestor
        higherDescendant = higherDescendant.ancestor
    return lowerDescendant
