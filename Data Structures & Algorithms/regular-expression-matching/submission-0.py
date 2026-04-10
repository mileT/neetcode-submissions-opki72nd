class Solution:
    def isMatchDFSmemo(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        memo = {}

        def dfs(i, j):
            if j == n:
                return i == m
            if (i, j) in memo:
                return memo[(i, j)]

            match = i < m and (s[i] == p[j] or p[j] == ".")
            if (j + 1) < n and p[j + 1] == "*":
                memo[(i, j)] = (dfs(i, j + 2) or (match and dfs(i + 1, j)))
                return memo[(i, j)]

            if match:
                memo[(i, j)] = dfs(i + 1, j + 1)
                return memo[(i, j)]

            memo[(i, j)] = False
            return memo[(i, j)]

        return dfs(0, 0)
    
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)] # dp[i][j] if s[i:] matches p[j:]

        dp[m][n] = True

        for i in range(m, -1, -1):
            for j in range(n - 1, -1, -1):
                curMatch = i < m and (s[i] == p[j] or p[j] == ".")
                if j + 1 < n and p[j + 1] == "*":
                    dp[i][j] = dp[i][j + 2] or (curMatch and dp[i + 1][j])
                else:
                    dp[i][j] = curMatch and dp[i + 1][j + 1]

        return dp[0][0]