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
        
        clone_map = {}
        clone_map[node] = Node(node.val)
        queue = deque([node])

        while queue:
            cur = queue.popleft()
            for neighbor in cur.neighbors:
                if neighbor not in clone_map:
                    clone_map[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                clone_map[cur].neighbors.append(clone_map[neighbor])

        return clone_map[node]
        