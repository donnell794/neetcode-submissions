"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        start = head
        nodes = {}
        prev = None
        while start:
            cp = Node(start.val)
            nodes[start] = cp
            if prev: nodes[prev].next = cp
            prev = start

            start = start.next
            cp = cp.next

        start = head
        while start:
            nodes[start].random = None if start.random is None else nodes[start.random]
            start = start.next

        
        return nodes[head] if head else head