class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # recursion 
        # recur(i, curlist)
        # base case
        # if i >= len(nums)
        #   add the cur list to res list
        
        # recursive case
        #   ## include
        #   curlist.append(nums[i])
        #   recur(i + 1)
        #   curlist.pop()
        #   recur(i + 1)

        # recur(0)
        # return res

        res = []
        subset = []
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return

            # recursive
            # include
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res