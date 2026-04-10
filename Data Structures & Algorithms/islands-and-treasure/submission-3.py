class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        visit = set()
        q = deque()

        def add_cell(r, c):
            if (r < 0 or r == m or c < 0 or c == n or (r, c) in visit or grid[r][c] == -1):
                return
            visit.add((r, c))
            q.append([r, c])

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))

        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                add_cell(r - 1, c)
                add_cell(r + 1, c)
                add_cell(r, c + 1)
                add_cell(r, c - 1)
            dist += 1
        