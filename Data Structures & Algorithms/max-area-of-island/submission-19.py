class DSU:
    def __init__(self, n: int):
        self.parents = list(range(n))
        self.size = [1] * n

    def find(self, u: int):
        if u != self.parents[u]:
            self.parents[u] = self.find(self.parents[u])
        return self.parents[u]

    def union(self, u: int, v: int) -> bool:
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False
        else:
            if self.size[pu] >= self.size[pv]:
                self.parents[pv] = pu
                self.size[pu] += self.size[pv]
            else:
                self.parents[pu] = pv
                self.size[pv] += self.size[pu]
            return True

    def getSize(self, u: int) -> bool:
        return self.size[self.find(u)]

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if (not grid or len(grid) == 0):
            return 0
        m, n = len(grid), len(grid[0])

        def index(i: int, j: int) -> int:
            return i * n + j

        dsu = DSU(m * n)
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        maxArea = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    # dsu.size[index(i, j)] = 1 if dsu.size[index(i, j)] == 0 else dsu.size[index(i, j)]
                    for dr, dc in directions:
                        x, y = i + dr, j + dc
                        if (x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 0):
                            continue
                        else:
                            # dsu.size[index(x, y)] = 1 if dsu.size[index(x, y)] == 0 else dsu.size[index(x, y)]
                            dsu.union(index(i, j), index(x, y))
                    maxArea = max(maxArea, dsu.getSize(index(i, j)))

        return maxArea



# class Solution:
#     def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
#         if (not grid or len(grid) == 0):
#             return 0
#         m, n = len(grid), len(grid[0])
#         result = 0
#         directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

#         def bfs(x: int, y: int) -> int:
#             q = deque()
#             area = 0
#             q.append((x, y))
#             grid[x][y] = 0

#             while q:
#                 r, c = q.popleft()
#                 area += 1
#                 for dr, dc in directions:
#                     nr, nc = r + dr, c + dc
#                     if (nr >= 0 and nr < m and nc >= 0 and nc < n and grid[nr][nc] == 1):
#                         q.append((nr, nc))
#                         grid[nr][nc] = 0
#             return area

#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == 1:
#                     result = max(result, bfs(i, j))

#         return result if result > 0 else 0

        # def dfs(x: int, y: int) -> int:
        #     if (x < 0 or x >= m or y < 0 or y >=n or grid[x][y] == 0):
        #         return 0
        #     else:
        #         cur = 1
        #         grid[x][y] = 0
        #         for dr, dc in directions:
        #             r, c = x + dr, y + dc
        #             cur += dfs(r, c)
        #         return cur

        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j] == 1:
        #             result = max(result, dfs(i, j))

        # return result if result > 0 else 0

            