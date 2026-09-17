class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # happy casds
        # intervals = [[1,2], [2,4], [1,6]]
        # output: 1

        # intervals = [[1,2], [2,4]]
        # output: 0

        # intervals = [[1,3], [2,4]]
        # output: 1

        # intervals = [[1,2], [1,2]]
        # output: 1

        # intervals = [[1,2],[1,2], [1,2]]
        # output: 2

        # sort the intervals based on the start
        # count  
        # prevEnd = end of the first interval
        # iterate thru every intervals
        #   check if the prevEnd > the start of the second interval
        #       increment the count
        #       set the prevEnd to the min of prevEnd and second interval end
        #   else
        #       set prevEnd to the second interval end

        intervals.sort(key=lambda x: x[0])
        count = 0
        prevEnd = intervals[0][1]

        for i in range(1, len(intervals)):

            if prevEnd > intervals[i][0]:
                count += 1
                prevEnd = min(prevEnd, intervals[i][1])
            else:
                prevEnd = intervals[i][1]

        return count
