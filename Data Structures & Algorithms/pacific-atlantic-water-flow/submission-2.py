class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        m, n = len(heights), len(heights[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        result = []
        pacificQ = deque([])
        atlanticQ = deque([])
        pacificMatrix = [[0] * n for _ in range(m)]
        atlanticMatrix = [[0] * n for _ in range(m)]

        def bfs(queue, matrix):
            while queue:
                x, y = queue.popleft()
                h = heights[x][y]
                matrix[x][y] = -1
                for dr, dc in directions:
                    r, c = x + dr, y + dc
                    if r >= 0 and r < m and c >= 0 and c < n and heights[r][c] >= h and matrix[r][c] != -1:
                        queue.append([r, c])
            return
        

        for i in range(m):
            pacificQ.append([i, 0])
            atlanticQ.append([i, n - 1])
        for j in range(n):
            pacificQ.append([0, j])
            atlanticQ.append([m - 1, j])
       
        bfs(pacificQ, pacificMatrix)
        bfs(atlanticQ, atlanticMatrix)

        # while pacificQ:
        #     x, y = pacificQ.popleft()
        #     h = heights[x][y]
        #     pacMatrix[x][y] = -1
        #     for dr, dc in dirs:
        #         r, c = x + dr, y + dc
        #         if r >= 0 and r < m and c >= 0 and c < n and heights[r][c] >= h and pacMatrix[r][c] != -1:
        #             pacificQ.append([r, c])

        # while atlanticQ:
        #     x, y = atlanticQ.popleft()
        #     h = heights[x][y]
        #     atlMatrix[x][y] = -1
        #     for dr, dc in dirs:
        #         r, c = x + dr, y + dc
        #         if r >= 0 and r < m and c >= 0 and c < n and heights[r][c] >= h and atlMatrix[r][c] != -1:
        #             atlanticQ.append([r, c])

        for i in range(m):
            for j in range(n):
                if pacificMatrix[i][j] == -1 and atlanticMatrix[i][j] == -1:
                    result.append([i, j])

        return result




        

        