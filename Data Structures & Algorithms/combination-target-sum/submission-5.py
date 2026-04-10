class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        cur = []
        curSum = 0

        def dfs(i, curSum):
            if i == len(nums) or curSum > target:
                return
            elif curSum == target:
                result.append(cur.copy())
            else:
                cur.append(nums[i])
                dfs(i,curSum + nums[i])
                cur.pop()
                dfs(i + 1, curSum)

        dfs(0, curSum)
        return result
            
        