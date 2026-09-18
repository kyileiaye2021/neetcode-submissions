class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # longest = 0
        # iterate thru the nums
        #   if n - 1 not in nums
        #       curr_longest = 1
        #   curr = n + 1
        #   while curr is in nums
        #       curr_longest += 1
        #       curr += 1
        #   longest = max(longest, curr_longest)
        # return longest

        nums = set(nums)
        longest = 0
        for n in nums:
            if n - 1 not in nums:
                curr_longest = 1

                curr = n + 1
                while curr in nums:
                    curr_longest += 1
                    curr += 1

                longest = max(longest, curr_longest)
        return longest
        
