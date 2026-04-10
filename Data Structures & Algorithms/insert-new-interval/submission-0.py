class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0

        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        
        start, end = newInterval[0], newInterval[1]
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            start = min(intervals[i][0], start)
            end = max(intervals[i][1], end)
            i += 1
        result.append([start, end])

        while i < len(intervals):
            result.append(intervals[i])
            i += 1

        return result
        