class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        maxArea = 0

        def dfs(grid, x, y) -> int:
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 0:
                return 0
            grid[x][y] = 0
            area = 1 + dfs(grid, x - 1, y) + dfs(grid, x + 1, y) + dfs(grid, x, y - 1) + dfs(grid, x, y + 1)
            return area
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area = dfs(grid, i, j)
                    maxArea = max(maxArea, area)

        return maxArea
