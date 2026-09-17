class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # happy cases
        # input: num = [1,1,2,3,4], val = 1
        # output: 3

        # edge cases
        # input: num = [1,1,2,3,4], val = 5
        # output: 5

        # Two pointer
        # i, j
        i, j = 0, 0

        while j < len(nums):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
            j += 1

        return i
        



