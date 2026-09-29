"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # sort by end time
        # iterate thru the intervals
        #   if curr start < prev end
        #       increment the meeting room

        # but this is just checking with prev interval and cannot reuse the room if the earlier meetings are done


        # we have to keep track of the active room that the meeting happens now

        # min heap {end time}
        # sort by end time
        
        # iterate thru the intervals
        #   while min heap and min heap[0] <= curr start
        #           pop the min heap
        #   add curr end time to min heap
        # return len(min heap)

        # O(nlogn)
        active_room = []
        sorted_intervals = sorted(intervals, key=lambda x: x.start)# need to sort by start time as the later meeting can pop the earlier meeting that should be still active.  
        max_room = 0

        for interval in sorted_intervals:
            while active_room and active_room[0] <= interval.start:
                heapq.heappop(active_room)
            heapq.heappush(active_room, interval.end)
            max_room = max(max_room, len(active_room))

        return max_room

        start = [interval.start for interval in intervals]
        end = [interval.end for interval in intervals]

        start.sort()
        end.sort()

        s = 0
        e = 0
        count = 0
        max_count = 0
        while s < len(start):
            if start[s] < end[e]:
                count += 1
                max_count = max(max_count, count)
                s += 1
            else:
                count -= 1
                e += 1

        return max_count
            

