class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs():
            q = deque()
            for r in range(m):
                for c in range(n):
                    if ((r == 0 or r == m - 1 or
                        c == 0 or c == n - 1) and
                        board[r][c] == "O"):
                        q.append((r, c))

            while q:
                r, c = q.popleft()
                if board[r][c] == "O":
                    board[r][c] = "#"
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < m and 0 <= nc < n:
                            q.append((nr, nc))

        bfs()
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "#":
                    board[i][j] = "O"
        