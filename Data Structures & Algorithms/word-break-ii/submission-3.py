class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # convert List to Dict for O(1) time check substr in dictionary
        wordDict = set(wordDict)
        result = []
        path = []
        n = len(s)

        def dfs(i, path):
            if i == n:
                # result.append(path.copy())
                result.append(" ".join(path))
                return
            for j in range(i, n):
                curWord = s[i: (j + 1)]
                if curWord in wordDict:
                    path.append(curWord)
                    dfs(j + 1, path)
                    path.pop()

        dfs(0, [])
        return result
        