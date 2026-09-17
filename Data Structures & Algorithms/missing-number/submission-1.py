class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        # in brute force - O(n)
        # find the max value form the nums
        # start from 0 and incrementing the num until the max value
        #   check if the curr num is not in the nums
        #       return that num

        # max_val = max(nums)
        # print(max_val)
        # i = 0

        # while i <= max_val:
        #     if i not in nums:
        #         return i
        #     i += 1

        # sort the arr - nlog(n)
        # iterate thru the arr from start 
        #   check if the curr ele is not 1 less than the next ele
        #       return the curr + 1
        # return 0

        # nums.sort()
        # for i in range(len(nums) - 1):
        #     if nums[i] != nums[i + 1] - 1:
        #         return nums[i] + 1

        # return 0

        # add all ele from 0 to n - O(n) time, O(1) space
        # and sum up all ele in the arr
        # subtract those two
        # n = len(nums)
        # total_sum = (n * (n + 1)) // 2
        # total = sum(nums)
        # return total_sum - total

        # xor solution
        n = len(nums)
        for i in range(len(nums)):
            n ^= i ^ nums[i]
        return n
        

        

