class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [] # pair of <temp, index>

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                top_value, top_index = stack.pop()
                result[top_index] = i - top_index
            stack.append((t, i))

        return result