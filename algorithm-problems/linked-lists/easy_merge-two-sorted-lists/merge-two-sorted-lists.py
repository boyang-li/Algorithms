
# LeetCode 21. Merge Two Sorted Lists

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Notes:
# The recursive approach. The recursive function always tries to find the next
# smallest node and link to it as the next node for the merged linked list.
#
# Complexity:
# O(m + n) time | O(m + n) space, where m and n are length of list1 and list2
def mergeTwoListsRec(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

    if list1 is None:
        return list2
    if list2 is None:
        return list1

    head = None
    if list1.val < list2.val:
        head = list1
        list1 = list1.next
    else:
        head = list2
        list2 = list2.next

    head.next = mergeTwoListsRec(list1, list2)

    return head

# Notes:
# The iterative approach improves the space complexity to constant space.
# In this approach, we keep track of the head of the new list, and the tail to
# add on to.
#
# Complexity:
# O(m + n) time | O(1) space, where m and n are length of list1 and list2
def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    head = ListNode()
    tail = head

    while list1 is not None and list2 is not None:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next

        tail = tail.next

    tail.next = list2 if list1 is None else list1

    return head.next
