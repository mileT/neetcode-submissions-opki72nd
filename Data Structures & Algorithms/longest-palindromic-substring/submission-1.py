class Solution:
    def longestPalindrome(self, s: str) -> str:
        result_idx, result_len = 0, 0
        n = len(s)

        dp = [[False] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    if result_len < (j - i + 1):
                        result_idx = i
                        result_len = j - i + 1
        
        return s[result_idx : result_idx + result_len]
        