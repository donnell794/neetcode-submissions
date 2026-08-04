# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        p_route = self.dfs(root, p, [])
        q_route = self.dfs(root, q, [])
        p_set = set(p_route)
        for x in reversed(q_route):
            if x in p_set:
                return x

    def dfs(self, root, node, path):
        if root.val == node.val:
            path.append(root)
            return path
        
        path.append(root)
        if node.val < root.val:
            return self.dfs(root.left, node, path)
        else:
            return self.dfs(root.right, node, path)