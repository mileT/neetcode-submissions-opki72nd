class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []
        i = 0

        while i < n and nums[i] <= 0:
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue

            target = -nums[i]
            j, k = i + 1, n - 1
            while j < k:
                curSum = nums[j] + nums[k]
                if curSum == target:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                elif curSum < target:
                    j += 1
                else: 
                    k -= 1
            i += 1

        return result