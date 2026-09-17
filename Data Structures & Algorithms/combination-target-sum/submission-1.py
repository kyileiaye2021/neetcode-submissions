class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        # brute force
        # iterate thru the ele (i)
        #   target = target - cur ith num
        #   iterate thru the ele (j)
        #      check if the target is in the nums:
        #           create a curr list of (ith, jth)
        #      target = target - cur jth num
        #       

        # backtracking
        # if the path sum becomes target, append the cur list to the res list

        # if i >= len(nums) or the path sum >= target, dead end --> backtrack

        # total = total + curr ith ele
        # call dfs on the total and i 
        # total = total - curr ith ele
        # call dfs on the total and i + 1

        res = []

        def backtrack(i, curr, total):
            # basecase
            if total == target:
                res.append(curr.copy())
                return 

            if i >= len(nums) or total > target:
                return 

            total += nums[i]
            curr.append(nums[i])
            backtrack(i, curr, total)

            total -= nums[i]
            curr.pop()
            backtrack(i + 1, curr, total)

        curr = []
        backtrack(0, curr, 0)
        return res


            