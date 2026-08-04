# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        back = slow.next
        prev = slow.next = None
        while back:
            nxt = back.next
            back.next = prev
            prev = back
            back = nxt

        front, back = head, prev
        while back:
            nextf, nextb = front.next, back.next
            front.next = back
            back.next = nextf
            front, back = nextf, nextb