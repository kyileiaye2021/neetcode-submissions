class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Brute Force - O(n^2)
        # nested for loop 

        # Binary search in each row  - O(mlogn)
        #   Iterate thru each row
        #       l,r
        #       until l passes r
        #           search mid index
        #           check if the mid ele is the same as target
        #               return mid
        #           update l or r

        # Binary search the first elements in each row - log(m*n)
        #   find the largest element less than or equal to the target
        #   get into the row
        #   use binary search again to that row to find the ele

        # low level pseudocode
        # lowest - 0
        # highest - m
        # desired_row = 0
        # until lowest passes highest:
        #   find mid index
        #   check if the mid ele is equal to the target
        #       return true
        #   if mid ele is greater than the target
        #       decrement the highest to mid - 1
        #   if mid ele is less than the target
        #       desired_row = max(desired_row, mid)
        #       increment the lowest to mid + 1

        # l,r = matrix[m][0], matrix[m][n-1]
        # until l passes r
        #   find mid index
        #   check if mid ele is equal to the target
        #       return true
        #   if mid ele is greater than target
        #       decrement r to mid -1
        #   otherwise: 
        #       increment l to mid+1

        # return false
        # m - size of row
        # n - size of columns

        m = len(matrix)
        lowest, highest = 0, m-1
        desired_row = 0
        while lowest <= highest:
            mid = (lowest + highest) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                highest = mid - 1

            else:
                desired_row = max(desired_row, mid)
                lowest = mid + 1

        print("desired:",desired_row)
        n = len(matrix[0])
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2

            if matrix[desired_row][mid] == target:
                return True
            elif matrix[desired_row][mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return False

        # Time complexity - O(log (m * n))
        # Space complexity - O(1)