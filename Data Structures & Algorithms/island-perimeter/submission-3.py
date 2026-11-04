class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visit = set()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def bfs(i, j):
            perimeter = 0
            queue = deque([(i, j)])
            visit.add((i, j))

            while queue:
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n:
                        if grid[nx][ny] == 1 and (nx, ny) not in visit:
                            visit.add((nx, ny))
                            queue.append((nx, ny))
                        elif grid[nx][ny] == 0:
                            perimeter += 1
                    else:
                        perimeter += 1

            return perimeter

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return bfs(i, j)
        
        return 0