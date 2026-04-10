class DSU:
    def __init__(self, n):
        self.Parent = list(range(n + 1))
        self.Size = [1] * (n + 1)

    def find(self, node):
        if self.Parent[node] != node:
            self.Parent[node] = self.find(self.Parent[node])
        return self.Parent[node]

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False
        if self.Size[pu] >= self.Size[pv]:
            self.Size[pu] += self.Size[pv]
            self.Parent[pv] = pu
        else:
            self.Size[pv] += self.Size[pu]
            self.Parent[pu] = pv
        return True
    
    def connected(self, u, v):
        return self.find(u) == self.find(v)

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        dsu = DSU(m * n + 1)

        for r in range(m):
            for c in range(n):
                if board[r][c] != "O":
                    continue
                if (r == 0 or c == 0 or r == m - 1 or c == n - 1):
                    dsu.union(m * n, r * n + c)
                else:
                    for dx, dy in directions:
                        nr, nc = r + dx, c + dy
                        if board[nr][nc] == "O":
                            dsu.union(r * n + c, nr * n + nc)

        for r in range(m):
            for c in range(n):
                if not dsu.connected(m * n, r * n + c):
                    board[r][c] = "X"
        