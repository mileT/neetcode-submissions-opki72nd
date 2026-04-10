# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def dfs(node):
            balanced = True
            if not node:
                return [True, 0]

            leftTree, rightTree = dfs(node.left), dfs(node.right)
            balanced = leftTree[0] and rightTree[0] and abs(leftTree[1] - rightTree[1]) < 2
            return [balanced, max(leftTree[1], rightTree[1]) + 1]

        return dfs(root)[0]
        