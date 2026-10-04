# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        cur = root

        def dfs(root):
            if not root:
                return
            else:
                root.left, root.right = root.right, root.left
                dfs(root.left)
                dfs(root.right)

        dfs(cur)
        return root
        