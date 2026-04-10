class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1
        water = (j - i) * min(heights[j], heights[i])
        while i < j:
            water = max(water, (j - i) * min(heights[i], heights[j]))
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return water
        