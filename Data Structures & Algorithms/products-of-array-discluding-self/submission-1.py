class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix, suffix = [1] * n, [1] * n

        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]
            suffix[n - 1 - i] = suffix[n - i ] * nums[n - i]
        
        result = [1] * n
        for i in range(n):
            result[i] = prefix[i] * suffix[i]

        return result
