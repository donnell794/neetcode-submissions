# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        start = prev = ListNode()
        carry = 0
        while l1 or l2:
            s = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            node = ListNode(s % 10)
            carry = s // 10
            prev.next = node

            if l1: l1 = l1.next
            if l2: l2 = l2.next
            prev = prev.next
            
        if carry: prev.next = ListNode(carry)
        return start.next