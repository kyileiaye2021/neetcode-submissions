class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # intervals = [[1,3],[1,5],[6,7]]
        # [1,5], [6,7]

        #  intervals = [[1,2],[2,3]]
        # [1,3]

        # intervals = [1,3],[4,5],[1,5]
        # [1,5]

        # sort the intervals by start
        # iterate thru the intervals from 2nd intervals
        #   check if the end of the last res >= curr interval start
        #       combine the 2 intervals and replace the last interval
        #   else:
        #       add the curr interval to res
        # return res

        res = []
        intervals.sort()

        for s, e in intervals:
            if res and res[-1][1] >= s:
                s = min(res[-1][0], s)
                e = max(res[-1][1], e)
            
                res[-1][0] = s
                res[-1][1] = e
            else:
                res.append([s, e])

        return res
            