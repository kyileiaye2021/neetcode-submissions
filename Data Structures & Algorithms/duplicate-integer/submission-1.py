class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # input: nums = [1,2,3,4]
        # output: false

        # input: nums = [1,2,3,3]
        # output: true

        # edge cases
        # input: nums = []
        # output: false

        # input: nums = [1]
        # output: false

        # set

        
        duplicate = set()
        for n in nums:
            if n in duplicate:
                return True
            duplicate.add(n)

        return False