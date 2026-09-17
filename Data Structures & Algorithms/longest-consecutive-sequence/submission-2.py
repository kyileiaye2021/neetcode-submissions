class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # input:nums = [0, 3, 2, 5, 4, 6, 1, 1]
        # output: [0, 1, 1, 2, 3, 4, 5, 6]

        # input: nums = []
        # output: 0

        # input: nums = [2]
        # output: 0

        # input: nums = [1, 20]
        # output: 0

        # traverse the arr and get the max ele in the nums
        # create a new arr of size max ele
        # iterate thru the nums and assign 1 to the pos of the nums ele
        # create a sec new arr and iterate thru the new arr and assign indices where we found 1
        # iterate thru the sec arr and check if the curr ele is 1 greater than the prev ele --> increment the count

        # if len(nums) == 0:
        #     return 0

        # max_ele = float('-inf')

        # for n in nums:
        #     max_ele = max(max_ele, n)

        # new_arr = [0] * (max_ele + 1)
 
        # for n in nums:
        #     new_arr[n] = 1
        
        # sorted_new_arr = []

        # for i, ele in enumerate(new_arr):
        #     if ele == 1:
        #         sorted_new_arr.append(i)

        # print(sorted_new_arr)
        # count = 0
        # for i in range(1, len(sorted_new_arr)):
        #     if sorted_new_arr[i] - sorted_new_arr[i - 1] == 1:
        #         count += 1

        # return count+1

        numSet = set(nums)
        longest = 0
        for n in numSet:

            if (n - 1) not in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1
                longest = max(longest, length)

        return longest
