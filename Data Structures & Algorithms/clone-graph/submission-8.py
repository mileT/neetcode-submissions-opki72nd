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

        # nodes hash map, node -> clonedNode
        nodesMap = {}

        # DFS to visit and clone graph
        def dfs(cur: Node) -> Node:
            if not cur:
                return None
            if cur in nodesMap:
                return nodesMap[cur] 
            else:
                nodesMap[cur] = Node(cur.val)
                for nei in cur.neighbors:
                    nodesMap[cur].neighbors.append(dfs(nei))

            return nodesMap[cur]

        return dfs(node)

        # # use BFS to visit and clone graph
        # q = deque()
        # q.append(node)

        # while q:
        #     curNode = q.popleft()
        #     for nei in curNode.neighbors:
        #         #check if nei node already cloned 
        #         if nei not in nodesMap:
        #             nodesMap[nei] = Node(nei.val)
        #             q.append(nei)
        #         nodesMap[curNode].neighbors.append(nodesMap[nei])

        # return nodesMap[node]

        