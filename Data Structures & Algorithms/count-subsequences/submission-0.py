class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(t) > len(s):
            return 0

        dp = {}

        def dfs(i, j):
            if j >= len(t):
                return 1
            if i >= len(s):
                return 0

            if (i, j) in dp:
                return dp[(i, j)]

            result = 0
            if s[i] == t[j]:
                result = dfs(i + 1, j) + dfs(i + 1, j + 1)
            else:
                result = dfs(i + 1, j)

            dp[(i, j)] = result
            return result

        return dfs(0, 0)

        