class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Input: nums = [2,-1,1,2], k = 2
        # output: 4

        # input: nums = [], k = 0
        # output: 0

        # Input: nums = [4,4,4,4,4,4], k = 4
        # output = 6

        # input: nums = [2, -1, -1, 2], k = -2
        # output: 1

        # sliding window / hashmap
        # create a hashmap
        # {prefix sum to be chopped up : count of that sum to be chopped up}
        # iterate thru the ele
        #   curr sum by adding the ele
        #   check if the curr sum - k is in the hashmap
        #       update the res
        #   add the curr sum to the hashmap and update the count

        prefix_Sum = {0 : 1}
        res = 0
        curr_sum = 0

        for n in nums:
            curr_sum += n

            diff = curr_sum - k

            if diff in prefix_Sum:
                res += prefix_Sum[diff]

            prefix_Sum[curr_sum] = prefix_Sum.get(curr_sum, 0) + 1
        
        return res

        # count = 0
        # curr_window_total = 0
        # j = 0

        # for i in range(len(nums)):

        #     curr_window_total += nums[i]
        #     if curr_window_total == k:
        #         count += 1
            
        #     while i > j and curr_window_total != k:
        #         curr_window_total -= nums[j]

        #         if curr_window_total == k:
        #             count += 1
        #         j += 1
            
        # return count
            






