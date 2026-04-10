class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        memo = {} # (index, total) -> # of ways

        def dfs(i, curSum):
            if i == len(nums):
                if curSum == target:
                    return 1
                else:
                    return 0

            if (i, curSum) in memo:
                return memo[(i, curSum)]

            memo[(i, curSum)] = dfs(i + 1, curSum + nums[i]) + dfs(i + 1, curSum - nums[i])
            return memo[(i, curSum)]

        return dfs(0, 0)
        