class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        visit = set()
        q = deque()

        def addCell(r, c):
            if (min(r, c) < 0 or r == m or c == n or (r, c) in visit or grid[r][c] == -1):
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
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist

                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)
            dist += 1
