class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def dfs(i: int, x: int, y: int, board: List[List[str]], word: str) -> bool:
            if i == len(word):
                return True

            if (x < 0 or x >= m or y < 0 or y >= n or word[i] != board[x][y]):
                return False

            board[x][y] = '*'
            if (dfs(i + 1, x - 1, y, board, word) or 
                dfs(i + 1, x + 1, y, board, word) or
                dfs(i + 1, x, y - 1, board, word) or
                dfs(i + 1, x, y + 1, board, word)):
                return True
            board[x][y] = word[i]

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(0, i, j, board, word):
                        return True

        return False