class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        n = len(nums)
        dp = [[0 for _ in range(n)] for _ in range(2)]

        dp[0][0] = 0
        dp[1][0] = nums[0]
        
        for i in range(1, n):
            dp[0][i] = max(dp[0][i - 1], dp[1][i - 1])
            dp[1][i] = dp[0][i - 1] + nums[i]

        return max(dp[0][n - 1], dp[1][n - 1])