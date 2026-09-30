class Solution:
    def rob(self, nums: List[int]) -> int:
        one = 0
        two = 0

        for n in nums:
            temp = two
            two = max(one + n, two)
            one = temp

        return two