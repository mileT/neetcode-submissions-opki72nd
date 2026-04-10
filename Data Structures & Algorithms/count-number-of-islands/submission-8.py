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
        if self.rank[pu] <= self.rank[pv]:
            self.parents[pu] = pv
            self.rank[pv] += 1
        else:
            self.parents[pv] = pu
            self.rank[pu] += 1
        return True

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        m, n = len(grid), len(grid[0])

        def index(i, j) -> int:
            return i * n + j

        dsu = DSU(m * n)
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    islands += 1

                    for dr, dc in directions:
                        x, y = i + dr, j + dc
                        if (x < 0 or y < 0 or x >=m or y >= n or grid[x][y] == "0"):
                            continue
                        if dsu.union(index(x, y), index(i, j)):
                            islands -= 1

        return islands


        