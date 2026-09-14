class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        removed = 0
        for index, num in enumerate(nums):
            if num != val:
                nums[removed] = num
                removed += 1
        return removed
        