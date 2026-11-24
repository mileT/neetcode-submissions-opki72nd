# You are given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.

# The test cases are generated so that the answer can fit in a 32-bit integer.

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1

        for curSum in range(1, target + 1):
            for num in nums:
                if curSum - num >= 0:
                    dp[curSum] += dp[curSum - num]

        return dp[target]
        