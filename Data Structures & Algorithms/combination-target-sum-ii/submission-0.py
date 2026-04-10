class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()

        def dfs(i, cur, total):
            if total == target:
                result.append(cur[:])
                return
            if total > target or i == len(nums):
                return

            cur.append(nums[i])
            dfs(i + 1, cur, total + nums[i])
            cur.pop()
                
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return result
        