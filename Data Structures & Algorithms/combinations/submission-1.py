class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def dfs(count, cur):
            if count == n + 1:
                if len(cur) == k:
                    result.append(cur.copy())
                return
            cur.append(count)
            dfs(count + 1, cur)
            cur.pop()
            dfs(count + 1, cur)

        dfs(1, [])
        return result
        