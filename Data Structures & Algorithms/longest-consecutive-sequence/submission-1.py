class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        result = 0

        for num in numsSet:
            if num - 1 not in numsSet:
                cur = 1

                while num + cur in numsSet:
                    cur += 1

                result = max(cur, result)

        return result
        