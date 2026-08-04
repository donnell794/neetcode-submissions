# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.traverse(p) == self.traverse(q)

    def traverse(self, root):
        if not root:
            return
        path = []
        queue = [root]
        while queue:
            node = queue.pop(0)
            path.append(node.val if node else None)
            if node is None:
                continue
            queue.extend([node.left, node.right])
        return path

        