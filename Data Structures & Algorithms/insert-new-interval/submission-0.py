class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # add the ele
        # sort the intervals
        # merge the intervals

        intervals.append(newInterval)
        intervals.sort()

        merged = [intervals[0]]

        for i in range(1, len(intervals)):
            curr_start = intervals[i][0]
            curr_end = intervals[i][1]

            prev_start = merged[-1][0]
            prev_end = merged[-1][1]

            if curr_start <= prev_end:
                merged[-1][0] = min(prev_start, curr_start)
                merged[-1][1] = max(prev_end, curr_end)
            else:
                merged.append([curr_start, curr_end])

        return merged