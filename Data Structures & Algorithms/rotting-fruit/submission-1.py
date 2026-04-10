class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])
        time = 0
        queue = deque([])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        freshCount = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append([i, j])
                if grid[i][j] == 1:
                    freshCount += 1

        while queue and freshCount > 0:
            time += 1
            for i in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in dirs:
                    x, y = r + dr, c + dc
                    if x >= 0 and x < m and y >= 0 and y < n and grid[x][y] == 1:
                        grid[x][y] = 2
                        queue.append([x, y])
                        freshCount -= 1
            
        
        return time if freshCount == 0 else -1
                


                    

        