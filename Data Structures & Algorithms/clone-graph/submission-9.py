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

        def dfs(curNode: Node) -> Node:
            if curNode in cloneMap:
                return cloneMap[curNode]
            cloneMap[curNode] = Node(curNode.val)
            for nei in curNode.neighbors:
                cloneMap[curNode].neighbors.append(dfs(nei))
            return cloneMap[curNode]

        return dfs(node)
        