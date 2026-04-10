class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.board = board
        self.result = []
        root = TrieNode()

        for word in words:
            node = root
            for letter in word:
                if letter not in node.children:
                    node.children[letter] = TrieNode()
                node = node.children[letter]
            node.word = word

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in root.children:
                    self.dfs(i, j, root)

        return self.result

    def dfs(self, row, col, parent):
        letter = self.board[row][col]
        cur_node = parent.children[letter]

        if cur_node.word:
            self.result.append(cur_node.word)
            cur_node.word = None
        
        self.board[row][col] = "#"
        row_offset = [-1, 0, 1, 0]
        col_offset = [0, 1, 0, -1]

        for i in range(4):
            r, c = row + row_offset[i], col + col_offset[i]
            if (r < 0 or r == len(self.board) or c < 0 or c == len(self.board[0])):
                continue
            if self.board[r][c] in cur_node.children:
                self.dfs(r, c, cur_node)
        
        self.board[row][col] = letter
        if not cur_node.children:
            del parent.children[letter]
        