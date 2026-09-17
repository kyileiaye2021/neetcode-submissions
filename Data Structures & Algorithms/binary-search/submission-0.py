class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # happy case
        # input - [-1,0,1], target = 0
        # output - 1

        # edge case
        # input - [-1, 0, 1], target = 2
        # output = -1

        # binary search

        # forward backward two pointers
        # l,r
        # until l passes r
        #   find the mid index
        #   check if the mid val is equal to target 
        #       return the mid index
        #   check if the mid val is greater than target
        #       move the r to the mid -1
        #   otherwise: move the l to the mid + 1

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] > target:
                r = mid - 1
            
            else:
                l = mid + 1

        
        return -1