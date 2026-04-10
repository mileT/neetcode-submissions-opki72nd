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

        queue = deque([node])
        cloneMap = {}
        cloneNode = Node(node.val)
        cloneMap[node] = cloneNode

        while queue:
            cur = queue.popleft()
            curClone = cloneMap[cur]
            # if cur not in cloneMap:
            #     copyNode = Node(cur.val)
            #     cloneMap[cur] = copyNode

            for nei in cur.neighbors:
                if nei not in cloneMap:
                    neiClone = Node(nei.val)
                    cloneMap[nei] = neiClone
                    queue.append(nei)
                curClone.neighbors.append(cloneMap[nei])
                

        return cloneMap[node]

        