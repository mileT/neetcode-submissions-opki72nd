class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
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
            
        