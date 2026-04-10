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

        cloned_map = {}
        cloned_map[node] = Node(node.val)
        queue = deque([node])

        while queue:
            cur = queue.popleft()
            for n in cur.neighbors:
                if n not in cloned_map:
                    cloned_map[n] = Node(n.val)
                    queue.append(n)
                cloned_map[cur].neighbors.append(cloned_map[n])
        
        return cloned_map[node]
        