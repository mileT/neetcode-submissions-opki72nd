class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        INF = 2147483647

        def bfs(r, c):
            q = deque([(r, c)])
            visit = [[False for _ in range(n)] for _ in range(m)]
            visit[r][c] = True
            steps = 0
            while q:
                for _ in range(len(q)):
                    row, col = q.popleft()
                    if grid[row][col] == 0:
                        return steps
                    for dr, dc in directions:
                        nr, nc = row + dr, col + dc
                        if (0 <= nr < m and 0 <= nc < n and
                            not visit[nr][nc] and grid[nr][nc] != -1):
                            visit[nr][nc] = True
                            q.append((nr, nc))
                steps += 1
            return INF

        for r in range(m):
            for c in range(n):
                if grid[r][c] == INF:
                    grid[r][c] = bfs(r, c)
        