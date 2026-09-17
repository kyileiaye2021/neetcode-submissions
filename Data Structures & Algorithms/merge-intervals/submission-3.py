class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort by start time
        # res = []
        # iterate thru the intervals
        #   prev_s = res[-1][0]
        #   prev_end = res[-1][1]
        #   check if the cur start < prev_end:
        #       res[-1][0] = min(cur_s, prev_s)
        #       res[-1][1] = max(cur_e, prev_e)
        #   else add the cur start and end to the res
        # return res

        res = []
        for s, e in sorted(intervals):
            if len(res) > 0:
                prev_s = res[-1][0]
                prev_e = res[-1][1]

                if s <= prev_e: # overlapped
                    res[-1][0] = min(s,prev_s)
                    res[-1][1] = max(e, prev_e)
                
                else:
                    res.append([s,e])
            else:
                res.append([s, e])

        return res


        