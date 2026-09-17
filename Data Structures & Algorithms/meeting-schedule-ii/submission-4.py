"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # sort by end time (nlogn)
        # prev end time

        # iterate thru the intervals
        #   if start time overlapped with prev end time
        #       increment room
        # return room.   

        intervals.sort(key=lambda x:x.start)
        min_heap = []

        for i in intervals:
            s, e = i.start, i.end
            if min_heap and min_heap[0] <= s:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, e)

        return len(min_heap)