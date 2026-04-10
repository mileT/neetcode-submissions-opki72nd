class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(i, total, cur):
            if i == len(nums) or total > target:
                return
            elif total == target:
                result.append(cur.copy())
                return
            else:
                cur.append(nums[i])
                dfs(i, total + nums[i], cur)
                cur.pop()
                dfs(i + 1, total, cur)

        dfs(0, 0, [])
        return result

        