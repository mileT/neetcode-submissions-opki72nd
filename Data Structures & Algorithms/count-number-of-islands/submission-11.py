class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return 0
        m, n = len(grid), len(grid[0])
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == "0":
                return

            grid[r][c] = "0"
            for dx, dy in dirs:
                x, y = r + dx, c + dy
                dfs(x, y)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    islands += 1
                    dfs(i, j)

        return islands    
        