# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        result = 0

        def dfs(root, maxVal):
            nonlocal result
            if not root:
                return
            
            if root.val >= maxVal:
                result += 1
                dfs(root.left,root.val)
                dfs(root.right, root.val)
            else:
                dfs(root.left, maxVal)
                dfs(root.right, maxVal)

        dfs(root, root.val)
        return result
        
        