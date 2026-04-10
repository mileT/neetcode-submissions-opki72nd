class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, u: int) -> int:
        if u != self.parent[u]:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v) -> bool:
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False
        
        if self.rank[pu] < self.rank[pv]:
            self.parent[pu] = pv
        elif self.rank[pu] > self.rank[pv]:
            self.parent[pv] = pu
        else:
            self.parent[pu] = pv
            self.rank[pv] += 1
        return True

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
            
        m, n = len(grid), len(grid[0])
        dsu = DSU(m * n)

        def index(r, c):
            return r * n + c

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        islands = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    islands += 1
                    for dr, dc in directions:
                        x, y = i + dr, j + dc
                        if (x < 0 or y < 0 or x >= m or y >= n or grid[x][y] == "0"):
                            continue
                        if dsu.union(index(i, j), index(x, y)):
                            islands -= 1

        return islands

        