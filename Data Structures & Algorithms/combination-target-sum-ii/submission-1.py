class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def dfs(i, cur, cur_sum):
            if cur_sum == target:
                result.append(cur.copy())
                return
            if cur_sum > target or i == len(candidates):
                return
            
            cur.append(candidates[i])
            dfs(i + 1, cur, cur_sum + candidates[i])
            cur.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, cur, cur_sum)

        dfs(0, [], 0)
        return result
        