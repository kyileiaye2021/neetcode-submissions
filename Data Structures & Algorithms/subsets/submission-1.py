class Solution:
    def backtrack(self, i, nums, curr_lst, res_lst):
        # base case
        # if the curr lst len becomes len of nums:
        #   append the curr lst to res lst
        if i >= len(nums):
            res_lst.append(curr_lst.copy())
            return

        # iterate thru the chars in nums??

        # include the curr i
        curr_lst.append(nums[i])
        # go to next ele
        self.backtrack(i + 1, nums, curr_lst, res_lst)

        # exclude the curr i
        curr_lst.pop()
        # go to next ele
        self.backtrack(i + 1, nums, curr_lst, res_lst)

    def subsets(self, nums: List[int]) -> List[List[int]]:

       # brute force - O(n^2) time
       # dfs-backtracking - O(2^n)
       curr_lst = []
       res_lst = []
       self.backtrack(0, nums, curr_lst, res_lst)
       return res_lst