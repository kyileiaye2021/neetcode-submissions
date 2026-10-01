class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        curList = []
        def dfs(i, total):
            # base case
            if total == target:
                res.append(curList.copy())
                return 

            if i >= len(candidates) or total > target:
                return

            # recursive case
            curList.append(candidates[i])
            dfs(i + 1, total + candidates[i])
            curList.pop()

            while i+1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            dfs(i + 1, total)


        dfs(0, 0)
        return res
