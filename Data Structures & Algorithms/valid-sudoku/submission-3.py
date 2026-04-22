class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m, n = len(board), len(board[0])
        rowDict = defaultdict(set)
        colDict = defaultdict(set)
        boxDict = defaultdict(set)

        for i in range(m):
            for j in range(n):
                cur = board[i][j]
                if cur == '.':
                    continue
                    
                if (cur in rowDict[i] or cur in colDict[j] or cur in boxDict[(i // 3, j // 3)]):
                    return False
                else:
                    rowDict[i].add(cur)
                    colDict[j].add(cur)
                    boxDict[(i // 3, j // 3)].add(cur)

        return True
        