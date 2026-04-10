class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        queue = deque()
        visit = set()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    queue.append((i,j))
                    visit.add((i, j))
        step = 0
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while queue:
            for k in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = step
                for dir in dirs:
                    row, col = r + dir[0], c + dir[1]
                    if (row >= 0 and row < m and col >= 0 and col < n 
                        and  (row, col) not in visit 
                        and grid[row][col] != -1):
                        # grid[row][col] = step + 1
                        visit.add((row, col))
                        queue.append((row, col))
            step += 1

        


        