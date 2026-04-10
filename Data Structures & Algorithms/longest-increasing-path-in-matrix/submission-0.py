class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        dp = {} # (r, c) -> LIP

        def dfs(r, c, preVal):
            if (min(r, c) < 0 or r >= m or c >= n or matrix[r][c] <= preVal):
                return 0

            if (r, c) in dp:
                return dp[(r, c)]

            result = 1
            for d in directions:
                result = max(result, 1 + dfs(r + d[0], c + d[1], matrix[r][c]))

            dp[(r, c)] = result
            return result

        for i in range(m):
            for j in range(n):
                dfs(i, j, -1)
                
        return max(dp.values())
        