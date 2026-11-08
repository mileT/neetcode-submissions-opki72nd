class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)

        def dfs(i):
            if i == len(s):
                result.append(" ".join(current))
                return
            for j in range(i, len(s)):
                w = s[i: (j + 1)]
                if w in wordDict:
                    current.append(w)
                    dfs(j + 1)
                    current.pop()
        
        current, result = [], []
        dfs(0)
        return result
        