class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        # intervals = [[1,3], [4,6]], newinterval = [2,5]
        # [[1,6]]

        # intervals = [[1,2],[3,5],[9,10]], newInterval = [6,7]
        # [[1,2],[3,5],[6,7],[9,10]]

        # intervals = [], new_interval = [1,3]
        # [[1,3]]

        # intervals= [[1,3],[4,6]], newInterval = [4,6]
        # [[1,3],[4,6]]

        # res = []
        # iterate thru thte intervals
        #   if the curr end < new interval start
        #       add the interval to res
        #   else:
        #       get the new start and end of interval
        #       assign it to res last ele
        # return res
        
        res = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]: # for intervals after newInterval
                res.append(newInterval)
                return res + intervals[i:]

            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])

            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]

        res.append(newInterval)
        return res
