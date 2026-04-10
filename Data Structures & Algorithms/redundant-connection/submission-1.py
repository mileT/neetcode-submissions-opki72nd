class DSU:
    def __init__(self, n):
        self.N = n
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)

    def find(self, node):
        cur = node
        while cur != self.parent[cur]:
            self.parent[cur] = self.parent[self.parent[cur]]
            cur = self.parent[cur]
        return self.parent[cur]

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
        dsu = DSU(n)
        for u, v in edges:
            if not dsu.union(u, v):
                return [u, v]

        
        