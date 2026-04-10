class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        best = 0
        for left in nums_set:
            if left - 1 not in nums_set:
                right = left + 1
                while right in nums_set:
                    right += 1
                best = max(best, right - left)
        return best
        