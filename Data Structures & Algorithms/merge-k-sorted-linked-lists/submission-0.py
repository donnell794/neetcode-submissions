# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __lt__(self, comp):
        return self.val < comp.val
    def __le__(self, comp):
        return self.val <= comp.val
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode()
        node = head
        heap = []
        for n in lists:
            heapq.heappush(heap, (n.val, n))

        while heap:
            nxt = heapq.heappop(heap)[1]
            node.next = nxt
            node = node.next
            if nxt.next:
                heapq.heappush(heap, (nxt.next.val, nxt.next))



        return head.next