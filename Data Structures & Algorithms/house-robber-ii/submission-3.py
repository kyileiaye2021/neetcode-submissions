class Solution:
    def findTotal(self, nums):
        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[-1]

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        # we have to separate because we can only choose which end side we will use
        first = nums[:len(nums) - 1]
        second = nums[1:]

        print(first)
        print(second)

        left_total = self.findTotal(first)
        right_total = self.findTotal(second)

        print(left_total)
        print(right_total)

        return max(left_total, right_total)


