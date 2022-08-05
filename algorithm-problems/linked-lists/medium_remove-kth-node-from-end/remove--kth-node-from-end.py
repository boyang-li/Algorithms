# O(n) time | O(1) space
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def removeKthNodeFromEnd(head, k):
    counter = 1
    first = head
    second = head
    # use two pinters, keep shifting the second pointer to the next node until
    # they are k nodes apart.
    while counter <= k:
        second = second.next
        counter += 1
    # if the second is out of bound, that means there are less than k nodes in
    # the linked list, the kth node from the end would be the head and we remove
    # the head node.
    if second is None:
        head.value = head.next.value
        head.next = head.next.next
        return
    # if the second is not the tail, we keep shifting both pointers until the
    # second pointer reaches the tail, and the first pointer would be at the kth
    # node from the tail.
    while second.next is not None:
        second = second.next
        first = first.next
    # remove the node at the first pointer.
    first.next = first.next.next
