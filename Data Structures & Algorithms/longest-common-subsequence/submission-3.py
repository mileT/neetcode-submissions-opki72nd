class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        memo =[ [-1] * n for _ in range(m)]

        def dfs(i, j) -> int:
            if i == m or j == n:
                return 0

            if memo[i][j] != -1:
                return memo[i][j]

            if text1[i] == text2[j]:
                memo[i][j] = dfs(i + 1, j + 1) + 1
            else:
                memo[i][j] = max(dfs(i + 1, j), dfs(i, j + 1))

            return memo[i][j]
            
        return dfs(0, 0)
        