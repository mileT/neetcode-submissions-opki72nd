class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        m, n  = len(grid),len(grid[0])
        visit = set()

        def dfs(x, y):
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 0:
                return 1
            if (x, y) in visit:
                return 0
            visit.add((x, y))
            return dfs(x - 1, y) + dfs(x + 1, y) + dfs(x, y - 1) + dfs(x, y + 1)

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    return dfs(i, j)
        return 0
        