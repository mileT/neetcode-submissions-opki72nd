class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj_list = {i : [] for i in range(n + 1)}

        for edge in edges:
            visit = [False] * (n + 1)
            src, target = edge[0], edge[1]
            if self.isConnected(src, target, visit, adj_list):
                return edge
            adj_list[src].append(target)
            adj_list[target].append(src)

        return []

    def isConnected(self, src, target, visit, adj_list):
        if src == target:
            return True
        
        visit[src] = True
        isFound = False

        for nei in adj_list[src]:
            if not visit[nei] and self.isConnected(nei, target, visit, adj_list):
                isFound = True

        return isFound 
        