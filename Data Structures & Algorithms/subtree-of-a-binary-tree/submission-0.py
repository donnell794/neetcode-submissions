# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        queue = [root]
        sub_root = self.tree(subRoot)
        while queue:
            node = queue.pop(0)
            if self.tree(node) == sub_root:
                return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return False

    def tree(self, root):
        res = []
        queue = [root]
        while queue:
            node = queue.pop(0)
            res.append(node.val if node else None)
            if node is None:
                continue
            queue.extend([node.left, node.right])
        return res