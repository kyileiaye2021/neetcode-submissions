class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # nums = [2, 3, -1, 3, 2]
        # output: 9

        # nums = [-2]
        # output: -2

        # nums = [0,0,0,0]
        # 0

        # nums = [9, -1, -5]
        # output: 9

        #bruteforce - O(n^2)
        # sliding window - O(n)

        r = 0
        total = 0
        max_sum = float('-inf')

        while r < len(nums):
            if total < 0:
                total = 0

            total += nums[r]
            max_sum = max(max_sum, total)
            r += 1

        return max_sum