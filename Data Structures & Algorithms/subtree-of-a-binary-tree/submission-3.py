# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        elif not root:
            return False
        elif  root != None and subRoot != None:
            return (self.isSametree(root, subRoot)
             or self.isSubtree(root.left, subRoot) 
             or self.isSubtree(root.right, subRoot))

    def isSametree(self, p, q) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
        else:
            return (p.val == q.val and 
                self.isSametree(p.left, q.left) and
                self.isSametree(p.right, q.right))
        