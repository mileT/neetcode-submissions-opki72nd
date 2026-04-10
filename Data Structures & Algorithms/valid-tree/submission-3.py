class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = {i : [] for i in range(n)}

        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)

      
        visit = set()

        def dfs(node, parent):
            if node in visit:
                return False

            visit.add(node)
            for nei in adjList[node]:
                if nei != parent:
                    if not dfs(nei, node):
                        return False
            return True

        return dfs(0, -1) and len(visit) == n
