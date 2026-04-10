class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        result = False

        for i in range(m):
            for j in range(n):
                if (board[i][j] == word[0]):
                    if (self.dfs(board, i, j, word, 0)):
                        return True
        
        return result

    def dfs(self, board, i, j, word, index):
        if (index == len(word)):
            return True
        if (i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[index] or board[i][j] == '*'):
            return False
        
        board[i][j] = '*'
        if_found_word = (self.dfs(board, i - 1, j , word, index + 1) or 
            self.dfs( board, i + 1, j, word, index + 1) or
            self.dfs( board, i, j - 1, word, index + 1) or
            self.dfs( board, i, j + 1, word, index + 1))
        board[i][j] = word[index]

        return if_found_word
        