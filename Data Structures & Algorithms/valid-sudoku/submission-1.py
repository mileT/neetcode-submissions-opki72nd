class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols, squares = defaultdict(set), defaultdict(set), defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                curStr = board[r][c]
                if (curStr in rows[r] or curStr in cols[c] or
                    curStr in squares[(r // 3, c // 3)]):
                    return False
                
                rows[r].add(curStr)
                cols[c].add(curStr)
                squares[(r // 3, c // 3)].add(curStr)
        
        return True

                
        