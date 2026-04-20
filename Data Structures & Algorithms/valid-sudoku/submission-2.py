class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m, n = len(board), len(board[0])
        rowDict = {i: set() for i in range(m)}
        colDict = {j: set() for j in range(n)}
        boxDict = defaultdict(set)

        for i in range(m):
            for j in range(n):
                if board[i][j] == '.':
                    continue
                else:
                    cur = board[i][j]
                    if (cur in rowDict[i] 
                        or cur in colDict[j] 
                        or cur in boxDict[(i // 3, j // 3)]):
                        return False
                    rowDict[i].add(cur)
                    colDict[j].add(cur)
                    boxDict[(i // 3, j // 3)].add(cur)

        return True
        