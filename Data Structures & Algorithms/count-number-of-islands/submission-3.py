class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        num_islands = 0
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def bfs(r, c):
            queue = collections.deque()
            queue.append((r, c)) # what is the function for add element to queue(deque)
     
            while queue:
                row, col = queue.popleft()
                grid[row][col] = "0"

                for dir in dirs:
                    x, y = row + dir[0], col + dir[1]
                    if x >= 0 and x < m and y >= 0 and y < n and grid[x][y] == "1":
                        queue.append((x, y))
                        # grid[x][y] = "0"

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    bfs(i, j)
                    num_islands += 1

        return num_islands
        