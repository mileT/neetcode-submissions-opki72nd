class DSU:
    def __init__(self, N):
        self.N = N
        self.size = [1] * N
        self.representative = list(range(N))

    def _find(self, node):
        if node != self.representative[node]:
            self.representative[node] = self._find(self.representative[node])
        return self.representative[node]
    
    def _union(self, node1, node2):
        rep1, rep2 = self._find(node1), self._find(node2)
        if rep1 == rep2:
            return False
        if self.size[rep1] < self.size[rep2]:
            rep1, rep2 = rep2, rep1
        self.size[rep1] += self.size[rep2]
        self.representative[rep2] = rep1
        return True
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        dsu = DSU(m * n)

        def index(r, c):
            return r * n + c
        
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        num_islands = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    num_islands += 1
                    for dr, dc in dirs:
                        r, c = i + dr, j + dc
                        if (r < 0 or r == m or c < 0 or c == n
                            or grid[r][c] == "0"):
                            continue
                        if dsu._union(index(i, j), index(r, c)):
                            num_islands -= 1
        
        return num_islands        