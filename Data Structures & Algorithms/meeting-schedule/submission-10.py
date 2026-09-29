"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # sort by start time
        # iterate thru the intervals
        #   if the start time is < prev end time
        #       return False
        # return true

        if not intervals:
            return True
        sorted_intervals = sorted(intervals, key=lambda x: x.start)  
        prev_end = sorted_intervals[0].end
        for interval in sorted_intervals[1:]:
            if interval.start < prev_end:
                return False
            prev_end = interval.end

        return True
