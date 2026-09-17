class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # given the array nums, we can do two passes to get prefix and postfix products
        # for prefix: default val - 1
        #             assign the prefix val to curr ele of nums
        #             update the prefix val with the product of prefix val and curr ele
        # for postfix: default val - 1
        #              assign the postfix val to curr ele 
        #              update the postfix val with the product of postfix val and curr ele

        # prefix and postfix values are updated in the res list (no need of prefix and postfix)

        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] *= prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res
