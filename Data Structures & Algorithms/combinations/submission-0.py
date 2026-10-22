class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def dfs(i, comb):
            if i > n:
                if len(comb) == k:
                    result.append(comb.copy())
                return
            comb.append(i)
            dfs(i + 1, comb)
            comb.pop()
            dfs(i + 1, comb)

        dfs(1, [])
        return result
            
        