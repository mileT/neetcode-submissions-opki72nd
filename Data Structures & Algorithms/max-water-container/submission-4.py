class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1
        result = 0

        while i < j:
            lowwer_height = min(heights[i], heights[j])
            result = max(result, lowwer_height * (j - i))
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1

        return result 
        