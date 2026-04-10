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
        cloneMap[node] = Node(node.val)
        q = deque([node])

        while q:
            curNode = q.popleft()
            for nei in curNode.neighbors:
                if nei not in cloneMap:
                    cloneMap[nei] = Node(nei.val)
                    q.append(nei)
                cloneMap[curNode].neighbors.append(cloneMap[nei])

        return cloneMap[node]

        