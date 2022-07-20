# A BST class for a Binary Search Tree. The class should support:
#  - Inserting values with the insert method.
#  - Removing values with the remove method; this method should only remove the first instance of a given value.
#  - Searching for values with the contains method.
# Note that you can't remove values from a single-node tree. In other words, calling the remove method on a
# single-node tree should simply not do anything.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Average: O(log(n)) time) | O(log(n)) space
    # Worst: O(n) time | O(n) space
    def insert(self, value):
        # if the value to be inserted is strictly smaller than the current node,
        # it has to go to he left subtree; Otherwise, go to the right subtree.
        if value < self.value:
            # if there is no left subtree, add the node as the left child
            # node, otherwise, call insert on the left child node recursively.
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
        return self

    # Average: O(log(n)) time) | O(log(n)) space
    # Worst: O(n) time | O(n) space
    def contains(self, value):
        if value < self.value: # go to the left subtree
            if self.left is None:
                return False
            else:
                return self.left.contains(value)
        elif value > self.value: # go to the right subtree
            if self.right is None:
                return False
            else:
                return self.right.contains(value)
        else: # value = self.value and we have found it
            return True

    # Remove is the most tricky operation for BST construction.
    # Essentially, whenever we have found the node to remove,
    # there are 4 cases we would face: 1. both children nodes exist; or
    # 2. the node itself is the root node; or 3. only one child node exists,
    # and the node it self is a left child node; or 4. only one child node
    # exists, and the node it self is a right child node;
    #
    # Average: O(log(n)) time) | O(log(n)) space
    # Worst: O(n) time | O(n) space
    def remove(self, value, parent=None):
        if value < self.value: # target is in the left child
            if self.left is not None: # left child exists
                self.left.remove(value, self) # recursively call
        elif value > self.value: # target is in the right child
            if self.right is not None: # right child exists
                self.right.remove(value, self) # recursively call
        else: # we have found the node to remove
            # case 1: both children exist
            if self.left is not None and self.right is not None:
                # replace current value with the min value in the right child
                self.value = self.right.getMinValue()
                # recursive call to remove the min value in the right child
                self.right.remove(self.value, self)
            # case 2: target node is the root node
            elif parent is None: # root node case
                if self.left is not None: # left child exists, replace self with left child
                    self.value = self.left.value
                    self.right = self.left.right
                    self.left = self.left.left
                elif self.right is not None: # right child exists, replace self with right child
                    self.value = self.right.value
                    self.left = self.right.left
                    self.right = self.right.right
                else: # single-node tree, do nothing
                    pass
            # case 3: the node to remove only has one child(could be either left or right),
            # and the node itself is a left child to its parent
            # finally set the node’s child as the left child to the parent
            elif parent.left == self:
                parent.left = self.left if self.left is not None else self.right
            # case 4: the node to remove only has one child(could be either left or right),
            # and the node itself is a right child to its parent
            # finally set the node’s child as the right child to the parent
            elif parent.right == self:
                parent.right = self.left if self.left is not None else self.right
            return self

    def getMinValue(self):
        if self.left is None:
            return self.value
        else:
            return self.left.getMinValue()
