class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
            
        m, n = len(grid), len(grid[0])
        result = 0

        def dfs(grid, x, y):
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == '0':
                return 
            
            grid[x][y] = '0'
            dfs(grid, x - 1, y)
            dfs(grid, x + 1, y)
            dfs(grid, x, y - 1)
            dfs(grid, x, y + 1)
            return
                
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    result += 1
                    dfs(grid, i, j)

        return result
        