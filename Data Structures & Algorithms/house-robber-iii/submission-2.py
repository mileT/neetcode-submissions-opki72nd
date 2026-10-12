# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        cache = dict()

        def dfs(node):
            if not node:
                return 0
            if node in cache:
                return cache[node]
            
            cur = node.val
            if node.left:
                cur += dfs(node.left.left) + dfs(node.left.right)
            if node.right:
                cur += dfs(node.right.left) + dfs(node.right.right)
            
            cache[node] = max(cur, dfs(node.left) + dfs(node.right))

            return cache[node]
        
        return dfs(root)