class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # happy cases
        # nums = [1,2,5,3]
        # output = 3 [1,2,3]

        # edge cases
        # nums = []
        # output = 0
        # nums = [5]
        # output = 1 [5]
        # nums = [5, 10]
        # output = 1 [5], [10]

        # create a set for the entire array
        # create a var called max_len to keep track of the max len the seq
        # iterate over each ele in the set:
        #   check if there is a left neighbor for the curr ele
        #       continue
        #   otherwise:
        #       create a list and create a var curr_len to keep track of the curr seq len
        #       add the curr ele to the list and increment the curr_len by 1
        #       while there are right neighbors in the set,
        #           add the curr ele to the list and increment the curr_len by 1
        #       update the max_len with max(counter, max_len)
        # return max_len

        nums = set(nums)
        max_len = 0

        for ele in nums:
            if ele - 1 in nums:
                continue

            else:
                curr_lst = []
                curr_len = 0
                curr_lst.append(ele)
                curr_len += 1

                ele += 1
                while ele in nums:
                    curr_lst.append(ele)
                    curr_len += 1
                    ele += 1

                max_len = max(curr_len, max_len)

        return max_len
