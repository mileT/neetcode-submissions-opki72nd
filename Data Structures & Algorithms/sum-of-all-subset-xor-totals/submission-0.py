class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        result = 0
        if not nums:
            return 0
        subsets = []

        def dfs(i, cur):
            if i == len(nums):
                subsets.append(self.xorSum(cur))
                return
            cur.append(nums[i])
            dfs(i + 1, cur)
            cur.pop()
            dfs(i + 1, cur)
        
        dfs(0, [])
        result = sum(subsets)
        return result 

    def xorSum(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result
        