class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = [0] * 2
        hash_map = dict()
        for i, num in enumerate(nums):
            second = target - num
            if second in hash_map:
                result = [hash_map.get(second), i]
            else:
                hash_map[num] = i
        return result