class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        queue = deque()
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for i in range(m):
            if board[i][0] == "O":
                queue.append([i, 0])
            if board[i][n - 1] == "O":
                queue.append([i, n - 1])

        for j in range(n):
            if board[0][j] == "O":
                queue.append([0, j])
            if board[m - 1][j] == "O":
                queue.append([m - 1, j])

        while queue:
            r, c = queue.popleft()
            board[r][c] = "*"
            for dr, dc in dirs:
                x, y = r + dr, c + dc
                if (x >= 0 and x < m and y >= 0 and y < n and board[x][y] == "O"):
                    queue.append([x, y])

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "*":
                    board[i][j] = "O"

        return


        