class DSU:
    def __init__(self, n):
        self.n = n
        self.parent = list(range(n))
        self.size = [1] * n
    
    def find(self, u) -> int:
        node = u
        while self.parent[node] != node:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return self.parent[node]

    def union(self, u, v) -> bool:
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False
        if self.size[pu] < self.size[pv]:
            pu, pv = pv, pu
        self.size[pu] += self.size[pv]
        self.parent[pv] = pu
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        dsu = DSU(n + 1)
        for u, v in edges:
            if not dsu.union(u, v):
                return [u, v]

        