"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # happy cases
        # intervals = [(0,40),(5,10),(15,20) ]
        # output: 2

        # intervals = [(0,5), (3, 6), (5, 10)]
        # output: 2

        # intervals = [(1,3), (3,5)]
        # output: 1

        # intervals = [(0,5)]
        # output: 1

        # intervals= []
        # output: 0

        # at the specific time, how many meetings are going on so we can know how many days we need
        # start time arr
        # end time arr 
        # s, e
        # iterate thru the arrs and 
        #   check if start time < end time
        #       increment the count
        #       move s by 1
        #   else
        #       decrement the count
        #       move e by 1
        # return count

        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        print(start)
        print(end)
        s = 0
        e = 0
        res = 0
        count = 0
        while s < len(start):
            if start[s] < end[e]: # the meeting started
                count += 1
                s += 1
            else:
                count -= 1
                e += 1
            res = max(count, res)
        return res
