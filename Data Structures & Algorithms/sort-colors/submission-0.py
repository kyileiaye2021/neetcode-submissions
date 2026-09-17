class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # input: nums = [1, 2, 0, 1, 2]
        # output: [0,1,1,2]
        
        # input: nums = [2, 0, 1]
        # output: [0, 1, 2]

        # input: nums = [2, 1]
        # output: [1, 2]

        # two pointers
        # l, r
        # l - index of the 0
        # r - index of. 2

        l, r = 0, len(nums) - 1
        i = 0

        while i <= r:
            
            if nums[i] == 2:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
                i -= 1

            elif nums[i] == 0:
                nums[i], nums[l] = nums[l], nums[i]
                l += 1

            i += 1

        return nums



