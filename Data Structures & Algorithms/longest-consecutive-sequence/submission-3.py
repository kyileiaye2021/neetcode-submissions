class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # nums = [2,20,4,10,3,4,5]
        # output: [2,3,4,5] 4

        # nums = [0,3,2,5,4,6,1,1]
        # output: [0,1,2,3,4,5,6] 7

        # sort the arr and put all ele in the set 
        # check if each ele is 1 greater than the prev ele

        # iterate thru the ele
        #   check if there is a left ele in the nums
        #       skip
        #   else:
        #       initialize the count 
        #       iterate thru from the starting point
        #           check if the curr ele in the nums
        #               increment the count
        #       update the max count
        # return max count

        max_count = 0
        for n in nums:
            if n-1 in nums:
                continue

            else:
                count = 0
                curr = n
                while curr in nums:
                    count += 1
                    curr += 1
                
                max_count = max(max_count, count)

        return max_count






