# Notes:
# We define a class for the Binary Search Tree data structure. The class should
# support the following operations:
#  - Insert: add new node for given value;
#  - Remove: delete node with given value(it removes the first occurrence);
#  - Search: return the node with given value;
#  - Contains: returns boolean whether the BST has a node with the given value.
#
# Note that you can't remove node from a single-node tree. In other words,
# calling the remove method on a single-node tree shouldn't do anything.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Average: O(log(n)) time) | O(log(n)) space
    # Worst: O(n) time | O(n) space
    def insert(self, value):
        # if the value to be inserted is strictly smaller than the current node,
        # it goes to the left subtree; Otherwise, it goes to the right subtree.
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

    # Average: O(log(n)) time | O(log(n)) space
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
        else:
            # value = self.value and we have found it
            return True

    # Remove is the most tricky operation for BST construction. When we have
    # found the node to remove, there are FOUR cases we would face:
    # 1. both child nodes exist;
    # 2. the current is the root node;
    # 3. only one of the child nodes exist, and the current node is a left child
    #    node to its parent;
    # 4. only one of the child nodes exist, and the current node is a right
    #    child node to its parent;
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
            # case 2: only one child exists, and target node is the root node
            elif parent is None:
                # left child exists, replace self with the left child node
                if self.left is not None:
                    self.value = self.left.value
                    self.right = self.left.right
                    self.left = self.left.left
                # right child exists, replace self with the right child node
                elif self.right is not None:
                    self.value = self.right.value
                    self.left = self.right.left
                    self.right = self.right.right
                else:
                    # single-node tree, do nothing
                    pass
            # case 3: only one child exists, and the target node itself is a
            # left child to its parent. we simply replace the target node with
            # its child node, in other words, the grand child becomes the child
            # to the parent.
            elif parent.left == self:
                parent.left = self.left if self.left is not None else self.right
            # case 4: silimiar to case 3, only this time target is the right
            # child to the parent.
            elif parent.right == self:
                parent.right = self.left if self.left is not None else self.right
            return self

    def getMinValue(self):
        if self.left is None:
            return self.value
        else:
            return self.left.getMinValue()
