class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(i, comb):
            if i == len(nums):
                result.append(comb.copy())
                return

            comb.append(nums[i])
            dfs(i + 1, comb)
            comb.pop()
            dfs(i + 1, comb)

        dfs(0, [])
        return result