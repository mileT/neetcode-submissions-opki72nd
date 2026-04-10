class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        cur = []

        def dfs(index, cur, pick):
            if index == len(nums):
                result.append(cur.copy())
                return
            
            for i in range(len(nums)):
                if not pick[i]:
                    cur.append(nums[i])
                    pick[i] = True
                    dfs(index + 1, cur, pick)
                    cur.pop()
                    pick[i] = False

        dfs(0, [], [False] * len(nums))
        return result

        