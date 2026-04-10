class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(x, y):
            board[x][y] = "*"
            for dr, dc in dirs:
                r, c = x + dr, y + dc
                if (r >= 0 and r < m and c >= 0 and c < n and board[r][c] == "O"):
                    dfs(r, c)

        for i in range(m):
            if board[i][0] == "O":
                dfs(i, 0)
            if board[i][n - 1] == "O":
                dfs(i, n - 1)
        for j in range(n):
            if board[0][j] == "O":
                dfs(0, j)
            if board[m - 1][j] == "O":
                dfs(m - 1, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "*":
                    board[i][j] = "O"

        return
        