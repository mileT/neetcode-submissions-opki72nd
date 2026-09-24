class TreeNode:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.buckets = [None] * self.size
    
    def _hash(self, key) -> int:
        return key % self.size
    
    def _bst_insert(self, root, key, val) -> TreeNode:
        if root is None:
            return TreeNode(key, val)
        if key == root.key:
            root.value = val
        elif key < root.key:
            root.left = self._bst_insert(root.left, key, val)
        else:
            root.right = self._bst_insert(root.right, key, val)
        return root
    
    def _bst_remove(self, root, key) -> TreeNode:
        if root is None:
            return None
        if key < root.key:
            root.left = self._bst_remove(root.left, key)
        elif key > root.key:
            root.right = self._bst_remove(root.right, key)
        else:
            #  root.value equals key, to remove current node
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            next = self._min_val_node(root.right)
            root.value = next.value
            root.key = next.key
            root.right = self._bst_remove(root.right, next.key)
        return root

    def _bst_search(self, root, key) -> TreeNode:
        if not root:
            return None
        else:
            if root.key == key:
                return root
            elif root.key > key:
                return self._bst_search(root.left, key)
            else:
                return self._bst_search(root.right, key)

    def _min_val_node(self, root) -> TreeNode:
        while root.left:
            root = root.left
        return root
        

    def put(self, key: int, value: int) -> None:
        index = self._hash(key)
        self.buckets[index] = self._bst_insert(self.buckets[index], key, value)

    def get(self, key: int) -> int:
        index = self._hash(key) 
        node = self._bst_search(self.buckets[index], key)
        return node.value if node else -1

    def remove(self, key: int) -> None:
        index = self._hash(key)
        self.buckets[index] = self._bst_remove(self.buckets[index], key)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)