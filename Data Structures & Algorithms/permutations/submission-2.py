class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        # [1,2]
        # [[1,2], [2,1]]

        # [1]
        # [[1]]

        # []
        # [[]]

        # temp list
        # res list
        # visited list (size nums)

        # backtrack
        # if the temp list becomes the size of res list
        #   append the copy of temp to the res list
        #   return

        # itereate thru the nums list
        #   if the curr num is not visited
        #       mark it as visited
        #       append it to the temp

        #       call backtrack

        #       mark it as unvisited
        #       pop it from the temp

        # return res

        res = []
        temp = []
        visited = [False] * len(nums)

        def backtrack():
            # base case
            if len(temp) == len(nums):
                res.append(temp.copy())
                return 

            for i in range(len(nums)):
                if not visited[i]:
                    visited[i] = True
                    temp.append(nums[i])

                    backtrack()

                    visited[i] = False
                    temp.pop()
        
        backtrack()
        return res

