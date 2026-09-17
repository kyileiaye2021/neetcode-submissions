class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def helper(arr):
            dp = [-1] * len(arr)
            def memo(i):
                # base case
                if i >= len(arr):
                    return 0

                if dp[i] != -1:
                    return dp[i]

                # rob the house
                rob = arr[i] + memo(i + 2)

                # skip the house
                skip = memo(i + 1)

                dp[i] = max(rob, skip)

                return dp[i]
        
            return memo(0)

        return max(helper(nums[:-1]), helper(nums[1:]))