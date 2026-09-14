class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        if n == 0:
            return 0
        
        i, j = 0, n - 1
        while i <= j: 
            while i < n and nums[i] != val:
                i += 1
            while j >= 0  and nums[j] == val:
                j -= 1
                
            if i > j:
                break

            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

        return i
