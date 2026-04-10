class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # result = 0
        # for num in nums:
        #     result = num ^ result
        # return result

        hash_set = set()

        for num in nums:
            if num in hash_set:
                hash_set.remove(num)
            else:
                hash_set.add(num)
        return hash_set.pop()
        