class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i in range(len(nums)):
            cur = nums[i]
            second = target - cur
            if second in num_map:
                return [num_map[second], i]
            num_map[cur] = i

        