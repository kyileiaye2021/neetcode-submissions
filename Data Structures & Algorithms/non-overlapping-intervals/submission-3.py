class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        last_end = intervals[0][0]
        count = 0

        for i, j in intervals:
            if i < last_end:
                last_end = min(last_end, j)
                count += 1
            else:
                last_end = j

        return count
        
       # sort the intervals

       # last end
       # iterate thru the intervals
       #    check if the curr interval start < last end:
       #        count += 1
       #    else
       #        last end = curr interval last end
       # return count

       