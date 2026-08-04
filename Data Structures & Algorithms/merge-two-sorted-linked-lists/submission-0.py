# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        first, second = list1, list2
        head = ListNode()
        node = head
        while first and second:
            if first.val <= second.val:
                node.next = first
                first = first.next
            else:
                node.next = second
                second = second.next
            node = node.next

        node.next = first if first else second
        return head.next
