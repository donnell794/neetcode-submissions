# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        start = ListNode()
        node = start.next = head

        l = 0
        while node:
            print(node.val)
            l += 1
            node = node.next

        node = start.next = head
        i, prev = 0, None
        while node and i < l-n:
            prev = node
            node = node.next
            i += 1

        prev = prev if prev else start
        prev.next = node.next

        return start.next