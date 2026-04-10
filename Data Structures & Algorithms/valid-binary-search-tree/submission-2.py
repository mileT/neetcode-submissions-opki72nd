# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def dfs(node, minVal, maxVal):
            if not node:
                return True

            if minVal < node.val < maxVal:
                return dfs(node.left, minVal, node.val) and dfs(node.right, node.val, maxVal)
            else:
                return False

        return dfs(root, float("-inf"), float("inf"))
        

        