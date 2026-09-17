class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        temp = []
        nums.sort()

        def backtrack(i):
            if i >= len(nums):
                res.append(temp.copy())
                return

            temp.append(nums[i])
            backtrack(i + 1)

            temp.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1)

        backtrack(0)

        return res