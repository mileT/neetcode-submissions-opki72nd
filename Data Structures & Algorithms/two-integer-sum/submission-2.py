class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for i in range(len(nums)):
            a, b = nums[i], target - nums[i]
            if b in hash_map:
                return [hash_map[b], i]

            hash_map[a] = i
        