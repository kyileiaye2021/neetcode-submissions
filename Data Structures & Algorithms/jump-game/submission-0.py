class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        # iterate thru the ele
        #   if the ele is greater than the remaining, 
        #       replace the ele with greater ele
        #   decrement the remaining
        # [1,2,0,1,0]
        remaining = 0

        for ele in nums:
            if remaining < 0:
                return False
            if ele > remaining:
                remaining = ele
            remaining -= 1
        return True
