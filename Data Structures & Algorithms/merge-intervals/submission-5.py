class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        res = [intervals[0]]

        for i in range(1, len(intervals)):
            if res[-1][1] >= intervals[i][0]:
                new_start = min(res[-1][0], intervals[i][0])
                new_end = max(res[-1][1], intervals[i][1])

                res[-1] = [new_start, new_end]
            else:
                res.append(intervals[i])

        return res