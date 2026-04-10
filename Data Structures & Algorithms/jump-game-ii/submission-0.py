class Solution:
    def jump(self, nums: List[int]) -> int:
        if not nums or len(nums) == 1:
            return 0

        n = len(nums)
        dp = [float('inf')] * n
        dp[-1] = 0

        for i in range(n - 2, -1, -1):
            # if nums[i] == 0:
            #     # dp[i] = -1
            #     continue
            for j in range(i + 1,  i + nums[i] + 1):
                # if dp[j] > 0:
                #     dp[i] = min(dp[i], dp[j] + 1)
                if j < n:
                    dp[i] = min(dp[i], dp[j] + 1)

        return dp[0] if dp[0] != float('inf') else -1
        