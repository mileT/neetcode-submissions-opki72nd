"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        cloneMap = {}

        def dfs(node):
            if node in cloneMap:
                return cloneMap[node]

            cloneNode = Node(node.val)
            cloneMap[node] = cloneNode

            for nei in node.neighbors:
                cloneNode.neighbors.append(dfs(nei))
            
            return cloneNode

        return dfs(node)

        