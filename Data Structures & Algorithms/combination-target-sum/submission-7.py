class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(i, cur, sum):
            if i == len(nums) or sum > target:
                return
            if sum == target:
                result.append(cur.copy())
                return
            cur.append(nums[i])
            dfs(i, cur, sum + nums[i])
            cur.pop()
            dfs(i + 1, cur, sum)

        dfs(0, [], 0)
        return result

        