# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.data = self.__traversal__(root)
        self.index = 0
  
    def __traversal__(self, node: TreeNode):
        output = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            output.append(node.val)
            dfs(node.right)
        dfs(node)
        return output
        

    def next(self) -> int:
        val = self.data[self.index]
        self.index += 1
        return val

    def hasNext(self) -> bool:
        return self.index < len(self.data) 


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()