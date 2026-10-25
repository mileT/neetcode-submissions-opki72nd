class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        for i in range(1 << n):
            cur = [nums[j] for j in range(n) if (i & (1 << j))]
            result.append(cur)
        return result
        