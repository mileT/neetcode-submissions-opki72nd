class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def bfs(i, j):
            q = deque([(i, j, 0)])
            while q:
                r, c, dis = q.popleft()
                for dr, dc in directions:
                    x, y = r + dr, c + dc
                    if (x >= 0 and x < m and y >= 0 and y < n and grid[x][y] > dis + 1):
                        grid[x][y] = dis + 1
                        q.append((x, y, dis + 1))
            return

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    bfs(i, j)

        return


        