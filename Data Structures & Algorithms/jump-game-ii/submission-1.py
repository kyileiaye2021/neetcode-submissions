class Solution:
    def jump(self, nums: List[int]) -> int:
        # l and r range
        # while r is less than or equal to the last index
            # in each pos in that range
            #   find the farthest index we can reach
            #   set l to r + 1
            #   set r to farthest index
            
        l = r = 0
        count = 0

        while r < len(nums) - 1:
            i = l 
            farthest = 0
            while i <= r:
                idx = i + nums[i]
                farthest = max(farthest, idx)
                i += 1
            count += 1
            l = r + 1
            r = farthest

        return count