class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i + 1][j + 1] + 1
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
        
        return dp[0][0]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        memo =[[-1] * n for _ in range(m)]

        def dfs(i: int, j: int) -> int:
            if i == m - 1 and j == n - 1:
                if text1[i] == text2[j]:
                    return 1
                else:
                    return 0
            if i >= m or j >= n:
                return 0

            if memo[i][j] != -1:
                return memo[i][j]

            if text1[i] == text2[j]:
                memo[i][j] = dfs(i + 1, j + 1) + 1
            else:
                memo[i][j] = max(dfs(i + 1, j), dfs(i, j + 1))

            return memo[i][j]

        return dfs(0, 0)
        