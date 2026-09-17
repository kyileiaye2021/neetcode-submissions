class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        # if the arr ele is only one len
        #   return that ele
        # if the arr ele is less than 3
        #   get the min ele and multiply it by 2
        #   compare the max ele with the min ele
        #   return the bigger one
        # total 
        # iterate thru the arr
        #   l = curr pos - 1
        #   r = curr pos + 1
        #   l count , r count = 0
        #   while the l pos is not out of bound
        #       check if the l ele is greater than or equal to the curr one
        #           increment the l count
        #   while the r pos is not out of bound
        #       check if the r ele is greater than or equal to the curr one
        #           increment the r count
        #   total = max(total, (curr + (l count * curr) + (r count * curr)))
        # return total

        if len(heights) == 0:
            return 0
        
        if len(heights) == 1:
            return heights[0]

        if len(heights) < 3:
            return max(max(heights), (min(heights) * 2))

        total = 0
        for i, h in enumerate(heights):
            l = i - 1
            r = i + 1
            l_count, r_count = 0, 0

            while l >= 0:
                if heights[l] >= heights[i]:
                    l_count += 1
                    l -= 1
                else:
                    break

            while r < len(heights):
                if heights[r] >= heights[i]:
                    r_count += 1
                    r += 1
                else:
                    break

            total = max(total, (heights[i] + (l_count * heights[i]) + (r_count * heights[i])))
        return total 
        
