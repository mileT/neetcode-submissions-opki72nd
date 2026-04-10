class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False

        m, n = len(board), len(board[0])

        def dfs(x, y, index):
            if index == len(word):
                return True
            if x < 0 or x == m or y < 0 or y == n or board[x][y] != word[index]:
                return False
            
            board[x][y] = '#'
            if (dfs(x + 1, y, index + 1) or
                dfs(x - 1, y, index + 1) or
                dfs(x, y + 1, index + 1) or
                dfs(x, y - 1, index + 1)):
                return True
            board[x][y] = word[index]

            return False
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True

        return False
        