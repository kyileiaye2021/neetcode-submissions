class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # edge case
        # [0,0,0,0]
        # 0

        # [2, 3]
        # 1

        # [2,2]
        # 0
        max_area = float('-inf')
        l = 0
        r = len(heights) - 1

        while l < r:
            curr_area = min(heights[l], heights[r]) * (r - l)    
            max_area = max(max_area, curr_area)    

            if heights[l] < heights[r]:
                l += 1

            else:
                r -= 1

        return max_area