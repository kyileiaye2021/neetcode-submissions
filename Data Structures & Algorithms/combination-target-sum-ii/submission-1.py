class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # happy cases
        # input: candidates = [9,2,2,4,6,1,5], target = 8
        # output: [[1,2,5], [2,2,4], [2,6]]

        # temp = [], res = []
        # total = 0
        # base case
        # if the total = target
        #   add the temp to res
        #   return 

        # if the total > target:
        #   return

        # add the ele to the temp
        # add teh curr ele to total 
        # call backtrack func on the next ele
        # remove the ele from temp
        # decrement the curr ele from total
        # call backtrack func on the next ele

        res = []
        temp = []
        total = 0
        candidates.sort()

        def backtrack(i, total):
            # base case
            if total == target:
                res.append(temp.copy())
                return

            if i >= len(candidates) or total > target:
                return

            temp.append(candidates[i])
            total += candidates[i]
            backtrack(i + 1, total)

            temp.pop()

            # check the duplicates
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            total -= candidates[i]
            backtrack(i+1, total)

        backtrack(0, total)
        return res
