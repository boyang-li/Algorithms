class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

## Naive solution ##
#
# O(h) time | O(h) space - where h is the height of the tree
def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
    # check if nodeThree <-- nodeTwo <-- nodeOne
    if isDescendant(nodeTwo, nodeOne):
        return isDescendant(nodeThree, nodeTwo)

    # check if nodeOne <-- nodeTwo <-- nodeThree
    if isDescendant(nodeTwo, nodeThree):
        return isDescendant(nodeOne, nodeTwo)

    return False

# check whether `target` is a descendant of the `node`
def isDescendant(node, target):
    if node is None:
        return False

    if node is target:
        return True

    return isDescendant(node.left, target) if target.value < node.value else isDescendant(node.right, target)

## Slightly improved solution ##
#
# O(h) time | O(1) space - where h is the height of the tree
def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
    # check if nodeThree <-- nodeTwo <-- nodeOne
    if isDescendant(nodeTwo, nodeOne):
        return isDescendant(nodeThree, nodeTwo)

    # check if nodeOne <-- nodeTwo <-- nodeThree
    if isDescendant(nodeTwo, nodeThree):
        return isDescendant(nodeOne, nodeTwo)

    return False

# check whether `target` is a descendant of the `node`
def isDescendant(node, target):
    while node is not None and node is not target:
        node = node.left if target.value < node.value else node.right

    return node is target


## Optimal solution ##
#
# O(d) time | O(1) space - where d is the distance between nodeOne and nodeThree
def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
    searchOne = nodeOne
    searchTwo = nodeThree

    while True:
        foundThreeFromOne = searchOne is nodeThree

        foundOneFromThree = searchTwo is nodeOne

        foundNodeTwo = searchOne is nodeTwo or searchTwo is nodeTwo

        finishSearching = searchOne is None and searchTwo is None

        if foundThreeFromOne or foundOneFromThree or foundNodeTwo or finishSearching:
            break

        if searchOne is not None:
            searchOne = searchOne.left if searchOne.value > nodeTwo.value else searchOne.right

        if searchTwo is not None:
            searchTwo = searchTwo.left if searchTwo.value > nodeTwo.value else searchTwo.right

    foundNodeFromOther = searchOne is nodeThree or searchTwo is nodeOne
    foundNodeTwo = searchOne is nodeTwo or searchTwo is nodeTwo

    # After the while loop above is finished, and we still have not found nodeTwo, or
    # nodeOne and nodeThree have meet eachOther, then it means that nodeTwo is not in
    # between nodeOne and nodeThree.
    if not foundNodeTwo or foundNodeFromOther:
        return False

    return searchForTarget(nodeTwo, nodeThree) if searchOne is nodeTwo else searchForTarget(nodeTwo, nodeOne)

def searchForTarget(node, target):
    while node is not None and node is not target:
        node = node.left if target.value < node.value else node.right

    return node is target
