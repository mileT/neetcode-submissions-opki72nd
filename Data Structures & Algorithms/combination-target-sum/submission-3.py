class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        cur = []

        def dfs(i, cur, cur_sum):
            if (cur_sum > target or i == len(nums)):
                return

            if (cur_sum == target):
                result.append(cur.copy())
                return
            
            cur.append(nums[i])
            dfs(i, cur, cur_sum + nums[i])
            cur.pop()
            dfs(i + 1, cur, cur_sum)

        dfs(0, [], 0)
        return result
        