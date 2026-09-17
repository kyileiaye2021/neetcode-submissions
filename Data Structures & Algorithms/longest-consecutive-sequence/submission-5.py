class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # happy cases
        # nums = [1, 20, 21, 23]
        # output: 2

        # nums = [3, 4, 5,6, 7]
        # output: 5

        # nums = [2, 6,9, 12]
        # output: 1

        # edge cases
        # nums = [1]
        # output: 1

        # nums = []
        # output: 0

        # sorting --> O(nlogn )
        # max count = 0
        # iterate thru the nums 
        #   check if the curr ele - 1 not in the nums:
        #       count = 1
        #       until the curr ele + 1 in the nums::
        #           increment the count
        #   update max count
        # return the max count 

        if len(nums) == 0:
            return 0
        max_count = 1
        for n in nums:
            if n - 1 not in nums:
                count = 1
                curr = n 
                while curr + 1 in nums:
                    count += 1
                    curr = curr + 1
            
                max_count = max(max_count, count)
        return max_count

