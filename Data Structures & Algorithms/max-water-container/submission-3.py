class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        max_area = 0

        while i < j:
            min_height = min(heights[i], heights[j])
            width = j - i
            curr_area = min_height * width
            max_area = max(max_area, curr_area)

            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1

        return max_area

