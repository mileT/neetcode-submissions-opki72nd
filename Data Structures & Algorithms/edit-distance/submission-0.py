class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
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


        