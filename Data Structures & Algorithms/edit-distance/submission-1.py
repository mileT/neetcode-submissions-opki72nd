class Solution:
    def minDistanceDFS(self, word1: str, word2: str) -> int:
        dp = {}

        def dfs(i: int, j: int) -> int:
            if j == len(word2):
                return len(word1) - i
            if i == len(word1):
                return len(word2) - j
                
            if (i, j) in dp:
                return dp[(i, j)]

            if word1[i] == word2[j]:
                return dfs(i + 1, j + 1)

            ops = min(dfs(i + 1, j), dfs(i, j + 1))
            ops = min(ops, dfs(i + 1, j + 1))
            dp[(i, j)] = ops + 1
            return dp[(i, j)]

        return dfs(0, 0)

    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[float("inf")] * (n + 1) for i in range(m + 1)]

        for i in range(m + 1):
            dp[i][n] = m - i
        for j in range(n + 1):
            dp[m][j] = n - j

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j + 1], dp[i + 1][j + 1])
        
        return dp[0][0]

        