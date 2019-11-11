class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if len(intervals) == 0:
            return 0
        intervals = sorted(intervals, key=lambda x: x[1])
        count = 1
        prev = 0
        for i in range(1, len(intervals)):
            curr = intervals[i]
            if intervals[prev][1] <= curr[0]:
                count += 1
                prev = i
        return len(intervals) - count
