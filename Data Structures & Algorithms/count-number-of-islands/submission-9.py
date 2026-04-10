class DSU:
    def __init__(self, n: int):
        self.parents = list(range(n))
        self.rank = [1] * n

    def find(self, u: int) -> int:
        if u != self.parents[u]:
            self.parents[u] = self.find(self.parents[u])
        return self.parents[u]

    def union(self, u: int, v: int) -> bool:
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False
        if self.rank[pu] >= self.rank[pv]:
            self.parents[pv] = pu
            self.rank[pu] += self.rank[pv]
        else:
            self.parents[pu] = pv
            self.rank[pv] += self.rank[pu]
        return True
        
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if (not grid or len(grid) == 0 or len(grid[0]) == 0):
            return 0
        m, n = len(grid), len(grid[0])
        islands = 0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def index(x, y):
            return x * n + y

        dsu = DSU(m * n)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    islands += 1
                    for dr, dc in directions:
                        r, c = i + dr, j + dc
                        if (r >= 0 and r < m and c >= 0 and c < n and grid[r][c] == "1"):
                            if dsu.union(index(i, j), index(r, c)):
                                islands -= 1

        return islands
                        


        
        