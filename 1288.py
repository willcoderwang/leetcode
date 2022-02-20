class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) < 2:
            return len(intervals)

        result = 1
        intervals.sort()
        max_r = intervals[0][1]
        l = intervals[0][0]
        for i in intervals[1:]:
            if i[1] > max_r:
                if i[0] > l:
                    result += 1
                max_r = i[1]
                l = i[0]

        return result
