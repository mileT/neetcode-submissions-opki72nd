class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque()
        minute = 0
        fresh_count = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append([i, j])
                if grid[i][j] == 1:
                    fresh_count += 1

        while q and fresh_count > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dir in directions:
                    row, col = r + dir[0], c + dir[1]
                    if (row >= 0 and row < m and col >= 0 and col < n and grid[row][col] == 1):
                        grid[row][col] = 2
                        fresh_count -= 1
                        q.append([row, col])
            minute += 1

        return minute if fresh_count == 0 else -1
        


        