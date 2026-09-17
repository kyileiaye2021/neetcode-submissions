class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # happy case
        # height = [1,3,8,2,9]
        # output = 16

        # edge case
        # height = [2,2,2]
        # output = 4

        # forward backward two pointers
        i, j = 0, len(heights) - 1

        max_area = float('-inf')

        while i < j:

            area = (j - i) * (min(heights[i], heights[j]))
            max_area = max(max_area, area)

            if heights[j] < heights[i]:
                j -= 1

            else:
                i += 1

        return max_area