class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # total = 0
        # max_total = -inf
        # iterate thru the ele
        #   add the curr ele to the total
        #   update the max total
        #   if total < 0
        #       reset total to 0
        # return max_total

        total = 0
        max_total = float('-inf')

        for n in nums:
            total += n
            max_total = max(max_total, total)

            if total < 0:
                total = 0

        return max_total
        