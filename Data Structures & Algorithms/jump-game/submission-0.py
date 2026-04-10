class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False
        n = len(nums)
        dp = [False] * n

        dp[n - 1] = True

        for i in range(n - 2, -1, -1):
            step = min(nums[i], n - 1 - i) 
            for j in range(1, step + 1):
                if dp[i + j]:
                    dp[i] = True
                    break

        return dp[0]