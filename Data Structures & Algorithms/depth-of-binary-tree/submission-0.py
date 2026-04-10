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

        return self.dfsNodesNum(root)

    def dfsNodesNum(self, node: TreeNode) -> int:
        if not node:
            return 0
        elif not node.left and not node.right:
            return 1
        else:
            return max(self.dfsNodesNum(node.left), self.dfsNodesNum(node.right)) + 1
        