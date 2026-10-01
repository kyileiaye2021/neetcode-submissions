class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        

        # dfs(i)
        # base case
        # if i >= len(nums) or total sum of curlist > target
        #   return
        # if total sum of curlist == target
        #   res.append(curlist.copy())
        #   return 

        # recursive case
        # add curr ele to cur list
        # dfs(i)
        # pop cur list
        # dfs(i + 1)

        res = []
        curlist = []
        def dfs(i, total):
            # base case
            if total == target:
                res.append(curlist.copy())
                return 
            if i >= len(nums) or total > target:
                return 

            # recursive case
            curlist.append(nums[i])
            dfs(i, total + nums[i])
            curlist.pop()
            dfs(i + 1, total)

        dfs(0, 0)
        return res


