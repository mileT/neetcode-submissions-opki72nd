class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}
        def dfs(curSum):
            if curSum == target:
                return 1
            elif curSum > target:
                return 0
            if curSum in memo:
                return memo[curSum]
            total = 0
            for num in nums:
                total += dfs(curSum + num)
            memo[curSum] = total
            return total
        return dfs(0)
        