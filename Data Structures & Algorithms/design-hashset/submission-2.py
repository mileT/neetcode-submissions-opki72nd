class TreeNode:
    def __init__(self, key: int):
        self.val = key
        self.left = None
        self.right = None

class MyHashSet:
    def __init__(self):
        self.size = 10**6
        self.buckets = [None] * self.size
    
    def _hash(self, key: int) -> int:
        return key % self.size
    
    def _bst_insert(self, root: TreeNode | None, key: int) -> TreeNode:
        if not root:
            return TreeNode(key)
        if key < root.val:
            root.left = self._bst_insert(root.left, key)
        elif key > root.val:
            root.right = self._bst_insert(root.right, key)
        
        return root
    
    def _bst_find(self, root: TreeNode | None, key: int) -> bool:
        if not root:
            return False
        if key == root.val:
            return True
        if key < root.val:
            return self._bst_find(root.left, key)
        else:
            return self._bst_find(root.right, key)
    
    def _bst_min(self, root: TreeNode) -> TreeNode:
        while root.left:
            root = root.left
        return root
    
    def _bst_remove(self, root: TreeNode | None, key: int) -> TreeNode | None:
        if not root:
            return None
        if key < root.val:
            root.left = self._bst_remove(root.left, key)
        elif key > root.val:
            root.right = self._bst_remove(root.right, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            next = self._bst_min(root.right)
            root.val = next.val
            root.right = self._bst_remove(root.right, next.val)
        return root


    def add(self, key: int) -> None:
        index = self._hash(key)
        self.buckets[index] = self._bst_insert(self.buckets[index], key)

    def remove(self, key: int) -> None:
        index = self._hash(key)
        self.buckets[index] = self._bst_remove(self.buckets[index], key)

    def contains(self, key: int) -> bool:
        index = self._hash(key)
        return self._bst_find(self.buckets[index], key)


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)