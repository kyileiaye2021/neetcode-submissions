class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # happy cases
        # intervals = [[1,3],[3,4],[4,5]]
        # output: [[1,5]]

        # intervals = [[1,3], [4,5], [7,8]]
        # output: [[1,3], [4,5], [7,8]]

        # intervals = [[1,5], [2,6]]
        # output: [[1,6]]

        # sort the arr based on the start time
        # res list - []
        # start - start time of the first ele
        # end - end time of the first ele
        # res list [[start, end]]
        # iterate thru the intervals
        #   curr start,  curr end time 
        #   check if the res list end >= curr start
        #       res list last ele start  = min(start, curr start)
        #       res list last ele end = max(end, curr end)
        #       res list = [[start, end]]
        #   else
        #       start = curr start
        #       end = curr end
        #       append the [start, end] to the res
        # return res

        intervals.sort()
        res = []
        if len(intervals) == 0:
            return res
        res.append(intervals[0])

        for i in range(1, len(intervals)):
            curr_start = intervals[i][0]
            curr_end = intervals[i][1]

            prev_start = res[-1][0]
            prev_end = res[-1][1]

            if curr_start <= prev_end:
                res[-1][0] = min(prev_start, curr_start)
                res[-1][1] = max(prev_end, curr_end)

            else:
                res.append([curr_start, curr_end])

        return res
