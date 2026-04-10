class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return [[]]
        intervals.sort(key=lambda i:i[0])
        output= [intervals[0]]


        for start, end in intervals[1:]:
            lastEnd = output[-1][1]

            if start > lastEnd:
                output.append([start, end])
            else:
                output[-1][1] = max(end, lastEnd)

        return output
        