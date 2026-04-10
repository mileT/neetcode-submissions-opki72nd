class DSU:
    def __init__(self, n):
        self.Parent = list(range(n + 1))
        self.Size = [1] * (n + 1)

    def find(self, u):
        if self.Parent[u] != u:
            self.Parent[u] = self.find(self.Parent[u])
        return self.Parent[u]
    
    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False
        if self.Size[pu] >= self.Size[pv]:
            self.Parent[pv] = pu
            self.Size[pu] += self.Size[pv]
        else:
            self.Parent[pu] = pv
            self.Size[pv] += self.Size[pu]
        return True

    def connected(self, u, v):
        return self.find(u) == self.find(v)

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        dsu = DSU(m * n + 1)
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for i in range(m):
            for j in range(n):
                if board[i][j] != "O":
                    continue

                if (i == 0 or i == m - 1 or j == 0 or j == n -1):
                    dsu.union(i * n + j, m * n)
                else:
                    for di, dj in dirs:
                        r, c = i + di, j + dj
                        if board[r][c] == "O":
                            dsu.union(r * n + c, i * n + j)

        for i in range(m):
            for j in range(n):
                if not dsu.connected(m * n, i * n + j):
                    board[i][j] = "X"

        return
        