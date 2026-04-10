class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        if not matrix or not matrix[0]:
            return

        m, n = len(matrix), len(matrix[0])
        rows, cols = [False] * m, [False] * n


        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows[i] = True
                    cols[j] = True

        for r in range(m):
            for c in range(n):
                if rows[r] or cols[c]:
                    matrix[r][c] = 0

        return
        
        