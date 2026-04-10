class Solution:
    def numDecodings(self, s: str) -> int:
        # Handle edge case where string is empty or starts with '0'
        if not s or s[0] == '0':
            return 0

        n = len(s)
        dp = [0] * (n + 1)
        dp[n] = 1  # There's one way to decode an empty substring
        
        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                dp[i] = 0  # No way to decode a string starting with '0'
            else:
                dp[i] = dp[i + 1]  # Decode using one character
                if i < n - 1 and (s[i] == '1' or (s[i] == '2' and s[i + 1] < '7')):
                    dp[i] += dp[i + 2]  # Decode using two characters

        return dp[0]

        