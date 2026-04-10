class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visit = [[0] * n for _ in range(m)]
        result = []

        def dfs(r, c, prev, mark):
            if (r < 0 or r == m or c < 0 or c == n or (visit[r][c] & mark == mark) or heights[r][c] < prev):
                return
            visit[r][c] |= mark
            if visit[r][c] == 3:
                result.append([r, c])
            for dx, dy in directions:
                dfs(r + dx, c + dy, heights[r][c], visit[r][c])

        for i in range(m):
            dfs(i, 0, -1, 1)
            dfs(i, n - 1, -1, 2)
        for j in range(n):
            dfs(0, j, -1, 1)
            dfs(m - 1, j, -1, 2)
        return result