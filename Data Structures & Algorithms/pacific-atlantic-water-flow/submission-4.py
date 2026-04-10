class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(i, j, matrix):
            matrix[i][j] = 1
            for dr, dc in dirs:
                r, c = i + dr, j + dc
                if (r >= 0 and r < m and c >= 0 and c < n and heights[r][c] >= heights[i][j] and matrix[r][c] != 1):
                    dfs(r, c, matrix)

        pacificMatrix = [[0] * n for _ in range(m)]
        atlanticMatrix = [[0] * n for _ in range(m)]
        result = []

        for i in range(m):
            dfs(i, 0, pacificMatrix)
            dfs(i, n - 1, atlanticMatrix)
        for j in range(n):
            dfs(0, j, pacificMatrix)
            dfs(m - 1, j, atlanticMatrix)

        for i in range(m):
            for j in range(n):
                if (pacificMatrix[i][j] == 1 and atlanticMatrix[i][j] == 1):
                    result.append([i, j])

        return result