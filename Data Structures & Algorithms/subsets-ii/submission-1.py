class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []

        def backtrack(i, curr):

            # base case
            if i >= len(nums):
                res.append(curr.copy())
                return 

            # include the curr ith num
            curr.append(nums[i])
            backtrack(i + 1, curr)

            # skip the duplicates
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            # exclude the curr ith num
            curr.pop()
            backtrack(i + 1, curr)

        curr = []
        backtrack(0, curr)
        return res