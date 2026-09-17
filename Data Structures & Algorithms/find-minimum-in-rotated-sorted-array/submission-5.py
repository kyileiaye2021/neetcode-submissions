class Solution:
    def findMin(self, nums: List[int]) -> int:
        # l , r
        # l = 0, r = last index
        # if l ele < r ele
        #   return l ele

        # while l <= r
        #
        # if l ele > r ele
        #   mid val 
        #   check if mid val >= l ele
        #       move l to mid + 1
        #   else 
        #       move r to mid
        # if l ele < r ele
        #       

        l = 0
        r = len(nums) - 1

        if nums[l] < nums[r]:
            return nums[l]

        while l <= r:
            if nums[l] < nums[r]:
                return nums[l]
            mid = (l + r) // 2
            if nums[mid] >= nums[l]:
                l = mid + 1

            else: 
                r = mid

        return nums[r]

