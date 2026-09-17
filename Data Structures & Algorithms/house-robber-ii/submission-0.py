class Solution:
    def rob(self, nums: List[int]) -> int:
        # we can't go over the adjacent ones
        # if the len of nums -> odd
        #   we have to check if the last one is adjacent to the first one
        if len(nums) == 1:
            return nums[0]

        return max(self.dp(nums[1:]), self.dp(nums[:len(nums) - 1]))

    def dp(self, nums): 
        first = 0
        second = 0

        for n in nums:
            # [first, second, n]
            new = max(first + n, second)
            first = second
            second = new

        return second