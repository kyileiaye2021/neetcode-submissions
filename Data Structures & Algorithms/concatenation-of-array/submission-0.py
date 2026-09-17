class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # happy cases
        # input: nums = [1, 4, 1, 2]
        # output: [1, 4, 1, 2, 1, 4, 1, 2]

        # edge cases
        # input: nums = []
        # output: []

        # input: nums = [2]
        # output: [2, 2]

        if len(nums) == 0:
            return []

        return nums * 2

        # time - O(n)
        # space - O(1)