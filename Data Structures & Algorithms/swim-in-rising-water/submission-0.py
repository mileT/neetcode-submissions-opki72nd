class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()
        pq = [(grid[0][0], 0, 0)]

        visited.add((0, 0))
        max_time = 0

        while pq:
            time, x, y = heapq.heappop(pq)
            max_time = max(time, max_time)
            if x == n - 1 and y == n - 1:
                return max_time
            for dx, dy in directions:
                r, c = x + dx, y + dy
                if (r >= 0 and r < n and c >= 0 and c < n and (r, c) not in visited):
                    visited.add((r, c))
                    heapq.heappush(pq, (max(time, grid[r][c]), r, c))

        return -1
        