class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        if not intervals or n == 0:
            return [newInterval]

        result = []
        i = 0
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        start, end = newInterval[0], newInterval[1]
        while i < n and intervals[i][0] <= newInterval[1]:
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])
            i += 1
        result.append([start, end])
        
        while i < n:
            result.append(intervals[i])
            i +=1
        
        return result
        