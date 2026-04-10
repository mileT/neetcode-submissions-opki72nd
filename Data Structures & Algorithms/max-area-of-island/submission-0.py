class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        result = 0

        def dfs(r, c):
            if (r < 0 or r == m or
                c < 0 or c == n or
                grid[r][c] != 1):
                return 0
            grid[r][c] = -1
            return 1 + dfs(r - 1, c) + dfs(r + 1, c) + dfs(r, c - 1) + dfs(r, c + 1)

        for i in range(m):
            for j in range(n):
                result = max(result, dfs(i, j))

        return result
        