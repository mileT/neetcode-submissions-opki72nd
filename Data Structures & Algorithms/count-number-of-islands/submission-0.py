class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])
        visited = set()
        islands = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            visited.add((r, c))
            while queue:
                row, col = queue.popleft()
                for dr, dc in directions:
                    x, y = row + dr, col + dc
                    if (x, y) not in visited and 0 <= x < m and 0 <= y < n and grid[x][y] == '1':
                        queue.append((x, y))
                        visited.add((x, y))


        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i, j) not in visited:
                    islands += 1
                    bfs(i, j)

        return islands
