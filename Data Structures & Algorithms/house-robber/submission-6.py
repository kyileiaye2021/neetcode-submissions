class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # nums = [1,1,3,3]
        # output: 4

        # nums = [2,9,8,3,6]
        # output: 16

        # nums = [5, 11, 2]
        # output: 11

        # nums = [5,1,1,8]
        # 13

        # brute force recursion / memoization
        # ith house (i)
        #   if i >= len(nums):
        #       return 0
        #   if dp[i] != -1:
        #       dp[i]
        #   # rob the house if we are allowed
        #       rob = nums[i] + rob(i + 2)
        #   # skip the house
        #       skip = rob(i + 1)
        #     dp[i] = max(rob, skip)
        #     return dp[i]

        # dp = [-1] * len(nums)
        # def memo(i):
        #     # base case
        #     if i >= len(nums):
        #         return 0

        #     if dp[i] != -1:
        #         return dp[i]

        #     # rob the house
        #     rob = nums[i] + memo(i + 2)

        #     # skip the house
        #     skip = memo(i + 1)

        #     dp[i] = max(rob, skip)

        #     return dp[i]

        # return memo(0)

        dp = [0] * (len(nums) + 1)
        dp[1] = nums[0]
        for i in range(1, len(nums)):

            # rob
            rob = nums[i] + dp[i - 1]

            # skip
            skip = dp[i]

            # max(rob, skip)
            dp[i + 1] = max(rob, skip)

        return dp[-1]
        