class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        # sort by start to check overlapping
        # prevEnd = first interval endtime
        # count = 0
        # iterate thru the intervals from second interval
        #   if curr start < prevEnd 
        #       get min val between prevEnd curr end
        #       count += 1
        #   else 
        #       set prevEnd to curr end
        # return count

        intervals.sort(key=lambda x: x[0])
        prevEnd = intervals[0][1]
        count = 0

        for start, end in intervals[1:]:
            if start < prevEnd:# if overlap
                prevEnd = min(prevEnd, end)
                count += 1
            else:
                prevEnd = end

        return count
