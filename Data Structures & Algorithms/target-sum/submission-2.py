class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        n = len(nums)
        memo = {}

        def dfs(i, path_sum):
            if i == n: 
             return 1 if target == path_sum else 0
            else:
                if (i, path_sum) in memo:
                    return memo[(i, path_sum)]
                else:
                    memo[(i, path_sum)] = dfs(i + 1, path_sum + nums[i]) + dfs(i + 1, path_sum - nums[i])
                    return memo[(i, path_sum)]

        return dfs(0, 0)

        