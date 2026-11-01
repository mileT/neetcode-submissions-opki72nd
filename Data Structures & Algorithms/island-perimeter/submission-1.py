class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visit = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def bfs(x, y):
            queue = deque([(x, y)])
            visit.add((x, y))
            perimeter = 0

            while queue:
                r, c = queue.popleft()
                for dx, dy in directions:
                    nx, ny = r + dx, c + dy
                    if (nx < 0 or ny < 0 or nx >= m or ny >= n or grid[nx][ny] == 0):
                        perimeter += 1
                    elif (nx, ny) not in visit:
                        visit.add((nx, ny))
                        queue.append((nx, ny))
            return perimeter

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return bfs(i, j)

        return 0
        