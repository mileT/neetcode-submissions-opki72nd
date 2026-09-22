import random

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def partition(low, high):
            pivot_idx = random.randint(low, high)
            nums[pivot_idx], nums[high] = nums[high], nums[pivot_idx]
            pivot = nums[high]

            i = low
            for j in range(low, high):
                if nums[j] < pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[high] = nums[high], nums[i]
            return i
        
        def quicksort(low, high):
            while low < high:
                p = partition(low, high)
                if p - low < high - p:
                    quicksort(low, p - 1)
                    low = p + 1
                else:
                    quicksort(p + 1, high)
                    high = p - 1

        quicksort(0, len(nums) - 1)
        return nums

        