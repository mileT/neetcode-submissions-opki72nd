class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        cur = []
        cur_sum = 0

        def dfs(i, total):
            if i == len(nums) or total > target:
                return
            elif total == target:
                result.append(cur.copy())
                return
            cur.append(nums[i])
            dfs(i, total + nums[i])
            cur.pop()
            dfs(i + 1, total)

        dfs(0, 0)
        return result
        