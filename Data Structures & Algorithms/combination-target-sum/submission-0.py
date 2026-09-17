class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # happy cases
        # nums = [2,5,6,9]
        # target = 9
        # output: [[5,2,2], [9]]

        # happy case
        # nums = [3,4,5]
        # target = 16
        # output; [[4,4,4,4], [3,4,4,5], [3,3,5,5], [3,3,3,3,4]]

        #. edge case
        # nums = []
        # target = 0
        # output: [[]]

        # nums = [3]
        # target = 6
        # output:[[3,3]]

        # nums = [3]
        # target = 5
        # output: []

        # backtracking
        # i = 0
        # res []
        # temp[]
        # backtrack func
        #   base case
        #   if the total == target:
        #       add the temp to the res
        #       return 
        #   if i >= nums len or total > target:
        #       return 
        # add the ele to the temp
        # call recursive func
        # pop out the ele from the temp
        # call recursive func on the next ele

        res = []
        temp = []
        total = 0
        def backtrack(i, total):
            # base case
            if total == target:
                res.append(temp.copy())
                return 

            if i >= len(nums) or total > target:
                return 

            temp.append(nums[i])
            total += nums[i]
            backtrack(i, total)

            temp.pop()
            total -= nums[i]
            backtrack(i + 1, total)
        
        backtrack(0, total)

        return res

