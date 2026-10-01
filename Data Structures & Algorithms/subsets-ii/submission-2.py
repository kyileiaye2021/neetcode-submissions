class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # sort the nums first
        # dfs recursion backtracking
        # res, cur list
        # recur(i)
        # base case
        #   if i >= len(nums)
        #       res.append(cur list copy)
        #       return 
        # recursive case
        #   cur list.append(nums[i])
        #   dfs(i + 1)
        #   cur list.pop()
        #   while i + 1 < len(nums) and nums[i] == nums[i + 1]
        #       i += 1
        #   dfs(i + 1)

        # recur(0)
        # return res
        nums.sort()
        res = []
        cur_lst = []

        def dfs(i):
            # base case
            if i >= len(nums):
                res.append(cur_lst.copy())
                return 

            # recursive case
            cur_lst.append(nums[i])
            dfs(i + 1)

            cur_lst.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            dfs(i + 1)

        dfs(0)
        return res