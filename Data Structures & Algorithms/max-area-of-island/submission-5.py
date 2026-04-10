class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])
        max_area = 0
        direactions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited = set()

        def bfs(x, y):
            queue = deque()
            queue.append((x, y))
            visited.add((x, y))
            area = 0

            while queue:
                row, col = queue.popleft()
                area += 1
                for dr, dc in direactions:
                    r, c = row + dr, col + dc
                    if (0 <= r < m and 0 <= c < n and
                        grid[r][c] == 1 and (r, c) not in visited):
                        visited.add((r, c))
                        queue.append((r, c))
            return area

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    cur_area = bfs(i, j)
                    max_area = max(max_area, cur_area)

        return max_area

        