class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:

        # happy case
        # nums = [1,2,3]
        # Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

        # nums = [1,2]
        # output: [[], [1], [2], [1,2]]

        # edge cases
        # nums = []
        # output: [[]]

        # nums = [1]
        # output: [[1]]

        # backtracking
        # res list
        # temp list
        # visited 

        # backtracking func
        # # base case
        # if len(tmp) == len(nums)
        #   return

        # iterate thru the list
        #   if the curr ele is not visited
        #       visit that ele
        #       add the ele to temp list
        #       add the temp list to the res
        #       backtrack
        #       pop the ele from temp list
        #       unvisit the ele

        res = []
        temp = []
        def backtrack(i):
            # base case
            if i >= len(nums):
                res.append(temp.copy())
                return

            temp.append(nums[i])
            backtrack(i + 1)

            temp.pop()
            backtrack(i + 1)

        backtrack(0)
        return res
