class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find which row to search for
        # select the row and apply binary search to find the target
        # l = 0
        # r = len(matrix) - 1
        # until l > r 
        #   mid = l + r // 2
        #   if mid ele == target
        #       return true
        #   elif target < mid ele
        #       r = mid - 1
        #   else:
        #       l = mid
        
        # iterate thru mid row ele
        # mid = l + r // 2
        # if mid ele == target
        #   return true
        # elif target < mid ele
        #   r = mid - 1
        # else
        #   l = mid + 1

        # return false

        rows = len(matrix)
        cols = len(matrix[0])

        l = 0
        r = rows - 1
        row_to_find = 0 
        while l <= r:
            mid = (l + r) // 2
            if matrix[mid][0] == target:
                return True
            elif target < matrix[mid][0]:
                r = mid - 1
            else:
                row_to_find = mid
                l = mid + 1
        
        l = 0
        r = cols - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[row_to_find][mid] == target:
                return True
            elif target < matrix[row_to_find][mid]:
                r = mid - 1
            else:
                l = mid + 1

        return False
            