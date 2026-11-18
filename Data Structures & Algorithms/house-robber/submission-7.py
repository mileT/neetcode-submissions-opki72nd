class Solution:
    def rob(self, nums: List[int]) -> int:
        rob2, rob1 = 0, 0

        for num in nums:
            temp = max(num + rob2, rob1)
            rob2 = rob1
            rob1 = temp
        return rob1
        