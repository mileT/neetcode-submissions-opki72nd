class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if not nums:
            return False
        nums.sort(reverse=True)
        totalSum = sum(nums)
        if totalSum % k != 0:
            return False

        target = totalSum // k
        used = [False] * len(nums)

        def dfs(i, k, subset):
            if k == 0:
                return True
            if subset == target:
                return dfs(0, k - 1, 0)
            for j in range(i, len(nums)):
                if used[j] or subset + nums[j] > target:
                    continue
                used[j] = True
                if dfs(j + 1, k, subset + nums[j]):
                    return True
                used[j] = False
            return False
        
        return dfs(0, k, 0)
        