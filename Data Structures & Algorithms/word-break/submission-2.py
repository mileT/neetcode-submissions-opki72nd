class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        t = 0
        for w in wordDict:
            t = max(t, len(w))
        
        dp = {}

        def dfs(i):
            if i in dp:
                return dp[i]
            if i == len(s):
                return True

            for j in range(i, min(len(s), i + t)):
                if s[i : j + 1] in wordSet:
                    if dfs(j + 1):
                        dp[i] = True
                        return True
            dp[i] = False
            return False

        return dfs(0) 