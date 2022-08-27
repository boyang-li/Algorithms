# LeetCode 2. Add Two Numbers

# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Complexity:
# O(max(m, n)) time | O(max(m, n)) space - where m and n are the length of l1 and l2 respectively.
def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummyHead = ListNode(0)
    curr = dummyHead
    carry = 0
    while l1 != None or l2 != None or carry != 0:
        l1Val = l1.val if l1 else 0
        l2Val = l2.val if l2 else 0
        colSum = l1Val + l2Val + carry
        carry = colSum // 10
        newNode = ListNode(colSum % 10)
        curr.next = newNode
        curr = newNode
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return dummyHead.next
