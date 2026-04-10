# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        leftDepath = self.maxDepth(root.left)
        rightDepath = self.maxDepth(root.right)
        return max(leftDepath, rightDepath) + 1
        