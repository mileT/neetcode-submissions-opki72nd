class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
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
        result = set()
        root = TrieNode()
        for word in words:
            root.addWord(word)
        
        visited = set()
        
        def dfs(r, c, node, word):
            if (r < 0 or r >= m or c < 0 or c >= n or (r, c) in visited or board[r][c] not in node.children):
                return
            
            visited.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                result.add(word)

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c - 1, node, word)
            dfs(r, c + 1, node, word)
            visited.remove((r, c))

        for r in range(m):
            for c in range(n):
                dfs(r, c, root, "")
            
        return list(result)
        