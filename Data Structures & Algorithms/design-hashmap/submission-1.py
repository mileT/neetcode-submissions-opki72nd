class TreeNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, key, val):
        if not root:
            return TreeNode(key, val)
        if key < root.key:
            root.left = self.insert(root.left, key, val)
        elif key > root.key:
            root.right = self.insert(root.right, key, val)
        else:
            root.val = val
        return root

    def delete(self, root, key):
        if not root:
            return None
        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            next_min = self.min_value_node(root.right)
            root.key = next_min.key
            root.val = next_min.val
            root.right = self.delete(root.right, next_min.key)
        return root

    def search(self, root, key):
        if not root:
            return None
        if key == root.key:
            return root.val
        elif key < root.key:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)

    def min_value_node(self, root):
        while root.left:
            root = root.left
        return root

class MyHashMap:

    def __init__(self):
        self.size = 1000  # much smaller; BST handles collisions fine
        self.buckets = [BST() for _ in range(self.size)]

    def put(self, key: int, value: int) -> None:
        index = key % self.size
        bst = self.buckets[index]
        bst.root = bst.insert(bst.root, key, value)

    def get(self, key: int) -> int:
        index = key % self.size
        bst = self.buckets[index]
        result = bst.search(bst.root, key)
        return result if result is not None else -1

    def remove(self, key: int) -> None:
        index = key % self.size
        bst = self.buckets[index]
        bst.root = bst.delete(bst.root, key)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)