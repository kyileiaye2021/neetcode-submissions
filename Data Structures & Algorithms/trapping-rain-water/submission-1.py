class Solution:
    def trap(self, height: List[int]) -> int:
        # happy case
        # Input: height = [0,2,0,3,1,0,1,3,2,1]

#        Output: 9
        # edge case
        # input: height = [1, 2, 3, 2, 1]
        # output: 0

        # two pointer
        # if the curr pointer is less than the next pointers, move the pointers
        # if it if greater --> subract the 

        if len(height) == 0:
            return 0
            
        l, r = 0, len(height) - 1
        res = 0

        maxLeft = height[l]
        maxRight = height[r]

        while l < r:
            if maxLeft < maxRight:
                l += 1
                maxLeft = max(maxLeft, height[l])
                res += maxLeft - height[l]

            else:
                r -= 1
                maxRight = max(maxRight, height[r])
                res += maxRight - height[r]

        return res
