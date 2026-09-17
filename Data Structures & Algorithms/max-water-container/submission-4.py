class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # happy cases
        # height = [1,7,2,5,4,7,3,6]
        # output: 36

        # height = [2,2,2]
        # output: 4

        # height = [1,1]
        # output: 1

        # edge cases
        # height = [0, 0]
        # output: 0

        # brute force - O(n^2)
        # two pointers - O(n)

        # l, r
        # max_area
        # while l < r:
        # check the curr area
        # go to higher height
        # keep track of max_area

        # return max_area

        l = 0
        r = len(heights) - 1
        max_area = 0

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            max_area = max(max_area, area)
            if heights[l] < heights[r]:
                l += 1

            else:
                r -= 1

        return max_area
        


        