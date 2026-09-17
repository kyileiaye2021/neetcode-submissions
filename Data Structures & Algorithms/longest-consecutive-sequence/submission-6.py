class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # nums  = [1, 2, 5, 7, 9]
        # output: 2

        # nums = [4,6,7,1,2,3,4,9,7,8,6,4,5]
        # output: 9

        # nums=[0,3,2,5,4,6,1,1]
        # 7
        # [0,1,2,3,4,5,6]

        # nums = [2,3,5,6,7,9,8]
        # output:5

        # nums = [1,3,5,7]

        # sort + drop the duplicates - O(nlogn) time
        
        max_len = 0
        nums = set(nums)
        for n in nums:
            # start of subseq
            if n - 1 not in nums:
                cur_len = 1
                start = n
                while start + 1 in nums:
                    cur_len += 1
                    start = start + 1

                max_len = max(cur_len, max_len)

        return max_len

