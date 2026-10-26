class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        cur = []

        def dfs(i):
            if i == len(nums):
                result.append(cur.copy())
                return

            cur.append(nums[i])
            dfs(i + 1)
            j = i
            while (j < len(nums) and nums[i] == nums[j]):
                j += 1
            cur.pop()
            dfs(j)

        dfs(0)
        return result
        