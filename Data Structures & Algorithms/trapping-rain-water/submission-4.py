class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        maxL = height[0]
        maxR = height[len(height) - 1]
        l = 0
        r = len(height) - 1
        
        while l < r:
            if maxL < maxR:
                l += 1
                diff = max(0, maxL - height[l])
                total += diff
                maxL = max(maxL, height[l])
            
            else: 
                r -= 1
                diff = max(0, maxR - height[r])
                total += diff
                maxR = max(maxR, height[r])

        return total 

