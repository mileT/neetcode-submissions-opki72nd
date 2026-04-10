class Solution:
    # def canJump(self, nums: List[int]) -> bool:
    #     if not nums:
    #         return False
    #     n = len(nums)
    #     dp = [False] * n

    #     dp[n - 1] = True

    #     for i in range(n - 2, -1, -1):
    #         end = min(n - 1, i + nums[i])
    #         for j in range(i + 1, end + 1):
    #             if dp[j]:
    #                 dp[i] = True
    #                 break

    #     return dp[0]
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False
        n = len(nums)

        def dfs(i: int) -> bool:
            if i == n - 1:
                return True
            if i >= n or nums[i] == 0:
                return False
            for j in range(1, nums[i] + 1):
                if dfs(i + j):
                    return True
            return False
        return dfs(0)