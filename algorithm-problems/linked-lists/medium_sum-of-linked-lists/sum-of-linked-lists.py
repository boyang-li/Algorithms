class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(max(m, n)) time | O(max(m, n)) space - where m and n are the lengths of the linked lists
def sumOfLinkedLists(linkedListOne, linkedListTwo):
    if linkedListOne is None:
        return linkedListTwo
    if linkedListTwo is None:
        return linkedListOne

    value = linkedListOne.value + linkedListTwo.value
    head = LinkedList(value % 10)
    carryOver = value // 10

    p1, p2, p3 = linkedListOne, linkedListTwo, head
    while p1.next is not None or p2.next is not None or carryOver > 0:
        print()
        if p1.next is not None:
            val1 = p1.next.value
            p1 = p1.next
        else:
            val1 = 0

        if p2.next is not None:
            val2 = p2.next.value
            p2 = p2.next
        else:
            val2 = 0
        valNext = val1 + val2 + carryOver
        nextNode = LinkedList(valNext % 10)
        carryOver = valNext // 10
        p3.next = nextNode
        p3 = p3.next
    p3.next = None

    return head
