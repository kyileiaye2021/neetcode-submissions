class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        # EXPANDING OUT THE ELEMENT FROM THE CURR POSITION 
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

        # if len(heights) == 0:
        #     return 0
        
        # if len(heights) == 1:
        #     return heights[0]

        # if len(heights) < 3:
        #     return max(max(heights), (min(heights) * 2))

        # total = 0
        # for i, h in enumerate(heights):
        #     l = i - 1
        #     r = i + 1
        #     l_count, r_count = 0, 0

        #     while l >= 0:
        #         if heights[l] >= heights[i]:
        #             l_count += 1
        #             l -= 1
        #         else:
        #             break

        #     while r < len(heights):
        #         if heights[r] >= heights[i]:
        #             r_count += 1
        #             r += 1
        #         else:
        #             break

        #     total = max(total, (heights[i] + (l_count * heights[i]) + (r_count * heights[i])))
        # return total 
        
        # USING STACK MONOTONIC INCREASING
        # iterate thru the ele in the arr
            # if the curr ele is greater than the last ele in stack
            #   add it to the stack with its index
            # else 
            #   while the last ele is smaller
            #       calculate the max total area  [(curr index - popped ele index) * popped ele] and pop. the ele out

        # iterate the ele in the stack
        #   calculate the max total area (len of heights - curr index) * curr ele 

        stack = []
        max_total = 0
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_total = max(max_total, (i - index) * height) 
                start = index
            
            stack.append((start, h))

        for idx, h in stack:
            max_total = max(max_total, (len(heights) - idx) * h)

        return max_total

        
