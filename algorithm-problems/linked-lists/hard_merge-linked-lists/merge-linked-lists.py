# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(m + n) time | O(1) - where m, n are the legnths of the two linked lists
def mergeLinkedLists(headOne, headTwo):
    if headOne is None:
        return headTwo
    if headTwo is None:
        return headOne

    head, currNode, pausedNode = None, None, None

    if headOne.value < headTwo.value: # start merge headTwo in headOne
        head = headOne
        currNode = headOne
        pausedNode = headTwo
    else:
        head = headTwo
        currNode = headTwo
        pausedNode = headOne

    while currNode.next is not None or pausedNode is not None:
        print("curr: ", currNode.value, " currNext: ", currNode.next.value if currNode.next is not None else 'None',
             " paused: ", pausedNode.value if pausedNode is not None else 'None')
        if currNode.next is None:
            currNode.next = pausedNode
            currNode = currNode.next
            pausedNode = None
        elif pausedNode is None or currNode.next.value < pausedNode.value:
            currNode = currNode.next
        else:
            tmpNextNode = currNode.next
            currNode.next = pausedNode
            pausedNode = tmpNextNode
            currNode = currNode.next

    return head
