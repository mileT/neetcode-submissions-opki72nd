class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = len(nums)

        # for i in range(len(nums)):
        #     result += i - nums[i]
        for i, num in enumerate(nums):
            result ^= i ^ num

        return result
        