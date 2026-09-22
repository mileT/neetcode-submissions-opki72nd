class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        temp = [0] * n

        def merge(low, mid, high):
            i, j = low, mid + 1
            k = low

            for index in range(low, high + 1):
                temp[index] = nums[index]

            for index in range(low, high + 1):
                if i > mid:
                    nums[index] = temp[j]
                    j += 1
                elif j > high:
                    nums[index] = temp[i]
                    i += 1
                elif temp[i] <= temp[j]:
                    nums[index] = temp[i]
                    i += 1
                else:
                    nums[index] = temp[j]
                    j += 1
        
        def sort(low, high):
            if low >= high:
                return
            mid = low + (high - low) // 2
            sort(low, mid)
            sort(mid + 1, high)
            merge(low, mid, high)

        sort(0, n - 1)
        return nums

        