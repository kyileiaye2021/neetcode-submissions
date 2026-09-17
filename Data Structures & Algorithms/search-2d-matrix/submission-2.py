class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # get the num row and num cols
        # l, r
        # l = 0
        # r = len(num row) -1
        rows = len(matrix)
        cols = len(matrix[0])
        l,r = 0, rows - 1
        target_row_index = -1

        while l <= r:
            mid_row = (l + r) // 2

            if target >= matrix[mid_row][0] and target <= matrix[mid_row][cols - 1]:
                target_row_index = mid_row
                break

            elif target > matrix[mid_row][cols - 1]:
                l = mid_row + 1

            else:
                r = mid_row - 1

        print(target_row_index)
        if target_row_index == -1:
            return False

        l = 0
        r = cols - 1

        while l <= r:
            mid = (l + r)// 2

            if matrix[target_row_index][mid] > target:
                r -= 1

            elif matrix[target_row_index][mid] < target:
                l += 1

            else:
                return True

        return False
        

