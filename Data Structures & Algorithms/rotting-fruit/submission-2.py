class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        time = 0
        freshOnes = 0
        queue = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                if grid[i][j] == 1:
                    freshOnes += 1

        while queue and freshOnes > 0:
            curQueueSize = len(queue)
            time += 1
            while curQueueSize:
                r, c = queue.popleft()
                for dr, dc in directions:
                    x, y = r + dr, c + dc
                    if (x >= 0 and x < m and y >= 0 and y < n and grid[x][y] == 1):
                        grid[x][y] = 2
                        freshOnes -= 1
                        queue.append((x, y))
                curQueueSize -= 1

        return time if freshOnes == 0 else -1
        