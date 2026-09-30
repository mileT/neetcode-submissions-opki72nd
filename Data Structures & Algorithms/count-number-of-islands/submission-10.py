class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, u) -> int:
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v) -> bool:
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False
        if self.rank[pu] >= self.rank[pv]:
            self.parent[pv] = self.parent[pu]
            self.rank[pu] += self.rank[pv]
        else:
            self.parent[pu] = self.parent[pv]
            self.rank[pv] += self.rank[pu]
        return True

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0
        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return 0
        
        m, n = len(grid), len(grid[0])
        dsu = DSU(m * n + 1)

        def index(x, y):
            return x * n + y

        def valid(x, y):
            return x >= 0 and x < m and y >= 0 and y < n and grid[x][y] == "1"

        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    result += 1
                    for dx, dy in dirs:
                        x, y = i + dx, j + dy
                        if valid(x, y):
                            if dsu.union(index(x, y), index(i, j)):
                                result -= 1

        return result
        