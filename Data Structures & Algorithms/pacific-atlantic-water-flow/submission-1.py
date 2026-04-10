class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        pac = [[False] * n for _ in range(m)]
        atl = [[False] * n for _ in range(m)]

        def bfs(source, ocean):
            q = deque(source)
            while q:
                r, c = q.popleft()
                ocean[r][c] = True
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < m and 0 <= nc < n and
                        not ocean[nr][nc] and
                        heights[nr][nc] >= heights[r][c]):
                        q.append((nr, nc))

        pacific, atlantic = [], []
        for c in range(n):
            pacific.append((0, c))
            atlantic.append((m - 1, c))

        for r in range(m):
            pacific.append((r, 0))
            atlantic.append((r, n - 1))

        bfs(pacific, pac)
        bfs(atlantic, atl)

        result = []
        for i in range(m):
            for j in range(n):
                if pac[i][j] and atl[i][j]:
                    result.append([i, j])

        return result

        