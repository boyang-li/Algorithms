# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(n) time | O(1) space - where n is the number of nodes in the Linked List
def reverseLinkedList(head):
    prev, curr = None, head
    while curr is not None:
        # the order of these steps matter.
        # first we set an variable to store the pointer to the next node of current node.
        next = curr.next
        # then we update the current's next to be its prev, or flipping the
        # direction of the node's bindings
        curr.next = prev
        # shift prev and curr forward along the linked list.
        prev = curr
        curr = next
    # now prev is the new head.
    return prev
