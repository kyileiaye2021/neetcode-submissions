class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        candidates.sort()

        def backtrack(i, curr, total):
            # base case
            if total == target:
                res.append(curr.copy())
                return 

            if i >= len(candidates) or total > target:
                return 

            total += candidates[i]
            curr.append(candidates[i])
            backtrack(i + 1, curr, total)

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            total -= candidates[i]
            curr.pop()
            backtrack(i + 1, curr, total)

        backtrack(0, [], 0)
        return res