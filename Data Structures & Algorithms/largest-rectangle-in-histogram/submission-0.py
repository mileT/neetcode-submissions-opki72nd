class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_sum, i = 0, 0
        while i < len(heights) or len(stack) > 0:
            if (len(stack) == 0 or (i < len(heights) and heights[i] > heights[stack[-1]])):
                stack.append(i)
                i += 1
            else:
                t = stack.pop()
                width = 0
                if len(stack) > 0:
                    width = i - stack[-1] - 1
                else:
                    width = i
                max_sum = max(max_sum, heights[t] * width)
        return max_sum
        