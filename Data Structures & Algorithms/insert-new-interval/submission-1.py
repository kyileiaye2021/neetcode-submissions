class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # add the ele
        # sort the intervals
        # merge the intervals
        res = []
        for i in range(len(intervals)):

            print(intervals[i])

            # if the new interval happens to be in front of every interval in the list
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i : ]

            # if new interval doesn't overlap with the current one
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])

            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]

        res.append(newInterval)
        return res

            