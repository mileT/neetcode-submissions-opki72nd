class Solution:
    #DP Top-Down or DFS with memo
    def isInterleave1(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        dp = {}
        
        def dfs(i, j, k):
            if k >= len(s3):
                return i == len(s1) and j == len(s2)

            if (i, j) in dp:
                return dp[(i, j)]
            
            result = False
            if i < len(s1) and s1[i] == s3[k]:
                result = dfs(i + 1, j, k + 1)
            
            if not result and j < len(s2) and s2[j] == s3[k]:
                result = dfs(i, j + 1, k + 1)

            dp[(i, j)] = result
            return dp[(i, j)]

        return dfs(0, 0, 0)

    # DP Bottom-Up
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        dp[len(s1)][len(s2)] = True

        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]:
                    dp[i][j] = True
                if j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]:
                    dp[i][j] = True
        
        return dp[0][0]
            
        