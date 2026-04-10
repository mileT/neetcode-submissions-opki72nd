class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWrod = Fasle
        self.refs = 0

    def addWord(self, word):
        cur = self
        cur.refs += 1
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
            cur.refs += 1
        cur.isWord = True

    def removeWord(self, word):
        cur = self
        cur.refs -= 1
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
                cur.refs -= 1

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        result = []

        def dfs(r, c, i, word):
            if i == len(word):
                return True
            if (r < 0 or r >= m or c < 0 or c >= n or board[r][c] != word[i]):
                return False

            board[r][c] = "*"

            findWord = dfs(r + 1, c, i + 1, word) or dfs(r - 1, c, i + 1, word) or dfs(r, c - 1, i + 1, word) or dfs(r, c + 1, i + 1, word)

            board[r][c] = word[i]
            return findWord

        for word in words:
            flag = False
            for r in range(m):
                if flag:
                    break
                for c in range(n):
                    if board[r][c] != word[0]:
                        continue
                    if dfs(r, c, 0, word):
                        result.append(word)
                        flag = True
                        break
        
        return result
        