# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast, slow = head, head
        start = True
        while fast and fast.next:
            if slow == fast:
                if start:
                    start = False
                else:
                    return True

            fast = fast.next.next
            slow = slow.next

        return False