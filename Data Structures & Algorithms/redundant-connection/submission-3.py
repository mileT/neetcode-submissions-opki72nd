class DSU:
    def __init__(self, n):
        self. N = n
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, node) -> int:
        cur = node
        while self.parent[cur] != cur:
            self.parent[cur] = self.parent[self.parent[cur]]
            cur = self.parent[cur]
        return self.parent[cur]

    def union(self, u, v) -> bool:
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False
        if self.size[pu] < self.size[pv]:
            pu, pv = pv, pu
        self.parent[pv] = pu
        self.size[pu] += self.size[pv]
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU(len(edges) + 1)
        for u, v in edges:
            if not dsu.union(u, v):
                return [u, v]
        