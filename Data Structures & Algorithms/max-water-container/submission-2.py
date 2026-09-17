class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # happy case
        # height = [1, 7, 2, 5, 4, 7, 3, 6]
        # output. = 36

        # two pointer
        max_area = 0
        i, j = 0, len(heights) - 1
        while i < j:
            width = j - i
            lower_bar = min(heights[i], heights[j])
            area = width * lower_bar
            max_area = max(area, max_area)

            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1

        return max_area