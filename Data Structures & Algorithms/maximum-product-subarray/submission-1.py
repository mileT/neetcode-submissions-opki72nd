class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n, result = len(nums), nums[0]
        prefix = suffix = 0

        for i in range(n):
            prefix = nums[i] * (prefix or 1)
            suffix = nums[n - 1 - i] * (suffix or 1)
            result = max(result, max(prefix, suffix))
            
        return result
        