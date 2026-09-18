class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        post = 1

        res = [1] * len(nums)

        for i in range(len(nums)):
            res[i] = pre #[1,1, 2, 8]
            pre = nums[i] * pre

        for i in range(len(nums) - 1, -1, -1):
            res[i] *= post # [48,24,12,8]
            post = nums[i] * post

        return res
