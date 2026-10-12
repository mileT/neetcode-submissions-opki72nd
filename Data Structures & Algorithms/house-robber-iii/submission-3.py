# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def dfs(node):
            if not node:
                return [0, 0]
            
            left_pair = dfs(node.left)
            right_pair = dfs(node.right)

            rob_cur = node.val + left_pair[1] + right_pair[1]
            not_rob_cur = max(left_pair) + max(right_pair)
            return [rob_cur, not_rob_cur]

        return max(dfs(root))
        