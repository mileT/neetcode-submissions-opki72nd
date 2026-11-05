class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        totalSum = sum(matchsticks)
        if totalSum % 4 != 0:
            return False
        n = len(matchsticks)
        matchsticks.sort(reverse=True)
        edgeLength = totalSum // 4
        used = [False] * n
        
        def dfs(i, k, curSum):
            if k == 0:
                return True
            if curSum == edgeLength:
                return dfs(0, k - 1, 0)
            for j in range(i, n):
                if used[j] or curSum + matchsticks[j] > edgeLength:
                    continue
                used[j] = True
                if dfs(j + 1, k, curSum + matchsticks[j]):
                    return True
                used[j] = False
            return False
        
        return dfs(0, 4, 0)
            