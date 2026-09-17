class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # happy case

        # nums = [1,2,4,6]
        # output: [48, 24, 12, 8]

        # nums = [-1, 0, 1]
        # output: [0, -1, 0]

        # nums = [-1, -2, -3]
        # output: [6, 3, 2]

        # nums = [0, 1]
        # output: [1, 0]


        # nested loop - O(n^2)
        # prefix, postfix O(n) space
        # optimal O(n) time O(1) space

        prefix = 1
        res = [0] * len(nums)

        # prefix update
        for i in range(len(nums)):
            res[i] = prefix
            prefix = prefix * nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] = res[i] * postfix
            postfix = postfix * nums[i]

        return res