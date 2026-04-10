class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        m, n = len(board), len(board[0])

        def dfs(index, r, c):
            if index == len(word):
                return True
            
            if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != word[index]:
                return False
            
            board[r][c] = '#'
            if (dfs(index + 1, r + 1, c) or
                dfs(index + 1, r - 1, c) or
                dfs(index + 1, r, c + 1) or 
                dfs(index + 1, r, c - 1)):
                return True
            board[r][c] = word[index]
            
            return False
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(0, i, j):
                        return True
        
        return False


        