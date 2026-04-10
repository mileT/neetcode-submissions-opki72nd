class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        indegrees = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                for d in directions:
                    r, c = i + d[0], j + d[1]
                    if (0 <= r < m and 0 <= c < n and matrix[r][c] < matrix[i][j]):
                        indegrees[i][j] += 1

        q = deque()
        for i in range(m):
            for j in range(n):
                if indegrees[i][j] == 0:
                    q.append([i, j])

        LIS = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for d in directions:
                    x, y = r + d[0], c + d[1]
                    if ( 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[r][c]):
                        indegrees[x][y] -= 1
                        if indegrees[x][y] == 0:
                            q.append([x, y])
            LIS += 1

        return LIS

        