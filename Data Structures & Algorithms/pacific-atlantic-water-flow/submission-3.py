class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def bfs(queue, matrix):
            while queue:
                x, y = queue.popleft()
                matrix[x][y] = -1
                h = heights[x][y]
                for dr, dc in directions:
                    r, c = x + dr, y + dc
                    if (r >= 0 and r < m and c >= 0 and c < n and heights[r][c] >= h and matrix[r][c] != -1):
                        queue.append((r, c))
            return

        pacificQueue, atlanticQueue = deque([]), deque([])
        pacificMatrix = [[0] * n for _ in range(m)]
        atlanticMatrix = [[0] * n for _ in range(m)]

        for i in range(m):
            pacificQueue.append((i, 0))
            atlanticQueue.append((i, n -1))
        for j in range(n):
            pacificQueue.append((0, j))
            atlanticQueue.append((m - 1, j))

        result = []
        bfs(pacificQueue, pacificMatrix)
        bfs(atlanticQueue, atlanticMatrix)

        for i in range(m):
            for j in range(n):
                if pacificMatrix[i][j] == -1 and atlanticMatrix[i][j] == -1:
                    result.append([i, j])

        return result
