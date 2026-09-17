class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # happy cases
        # nums = [1,2,3]
        # output: [1,2, 3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]

        # backtracking 
        # temp list
        # res list
        # visted list [F, F, F]

        # base case :
        # if len of the temp list == nums
        #   add the temp list to the res list
        #   return

        # iterate thru the list
        #   add the curr ele to the temp
        #   visit the curr ele
        #   call recursive func
        #   pop curr ele from the temp
        #   change the curr index false in visited

        # return the res list
        temp = []
        res = []
        visited = [False] * len(nums)

        def backtrack():

            # base case
            if len(temp) == len(nums):
                res.append(list(temp))
                return

            for i, ele in enumerate(nums):
                if not visited[i]:
                    # do the curr task
                    visited[i] = True
                    temp.append(ele)

                    backtrack()
                    
                    # undo the curr task
                    visited[i] = False
                    temp.pop()

        backtrack()
        return res
