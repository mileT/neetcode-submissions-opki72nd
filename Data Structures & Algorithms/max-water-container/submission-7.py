class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        result = 0

        while l < r:
            curArea = (r - l) * min(heights[l], heights[r])
            result = max(result, curArea)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

        return result


        