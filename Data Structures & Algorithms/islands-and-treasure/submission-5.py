class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return

        m, n = len(grid), len(grid[0])
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def bfs(grid, x, y):
            queue = deque([[x, y, 0]])
            while queue:
                r, c, val= queue.popleft()
                for dr in dirs:
                    nr, nc = r + dr[0], c + dr[1]
                    if nr >= 0 and nr < m and nc >= 0 and nc < n and grid[nr][nc] > val + 1:
                        grid[nr][nc] = min(grid[nr][nc], val + 1)
                        queue.append([nr, nc, grid[nr][nc]])

            return

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    bfs(grid, i, j)

        return



        