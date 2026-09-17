class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # if there are 2 houses, return the max one

        # start from house 3

        # [1, 2, 3]

        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[-1]
            
        if len(nums) == 2:
            return max(nums[-1], nums[-2])

        nums[1] = max(nums[1], nums[0])

        for i in range(2, len(nums)):
            nums[i] = max(nums[i] + nums[i - 2], nums[i - 1])

        return nums[-1]