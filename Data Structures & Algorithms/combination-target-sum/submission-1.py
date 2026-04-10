class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()

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

                while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                    i += 1
                dfs(i + 1, total, cur)

        dfs(0, 0, [])
        return result

        