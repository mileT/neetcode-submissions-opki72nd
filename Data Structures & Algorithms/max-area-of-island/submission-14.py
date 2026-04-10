class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if (not grid or len(grid) == 0):
            return 0
        m, n = len(grid), len(grid[0])
        result = 0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def bfs(x: int, y: int) -> int:
            q = deque()
            area = 0
            q.append((x, y))
            grid[x][y] = 0

            while q:
                r, c = q.popleft()
                area += 1
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr >= 0 and nr < m and nc >= 0 and nc < n and grid[nr][nc] == 1):
                        q.append((nr, nc))
                        grid[nr][nc] = 0
            return area

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    result = max(result, bfs(i, j))

        return result if result > 0 else 0

        # def dfs(x: int, y: int) -> int:
        #     if (x < 0 or x >= m or y < 0 or y >=n or grid[x][y] == 0):
        #         return 0
        #     else:
        #         cur = 1
        #         grid[x][y] = 0
        #         for dr, dc in directions:
        #             r, c = x + dr, y + dc
        #             cur += dfs(r, c)
        #         return cur

        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j] == 1:
        #             result = max(result, dfs(i, j))

        # return result if result > 0 else 0

            