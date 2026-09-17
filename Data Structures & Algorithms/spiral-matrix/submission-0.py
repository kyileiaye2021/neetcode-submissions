class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # l, r, t, b
        # l and t = 0
        # r = num of cols
        # b = num of rows
        # res list

        # while l < r and t < b
            #iterate thru the top row from l to r
            #   add the ele to the res lst
            # l += 1

            # iterate thru the right col from r - 1 to b - 1
            #   add the ele to the res lst
            # r -= 1

            # iterate thru the bottom row from r to l
            #   add the ele to res lst
            # b -= 1

            # iterate thru the left col from b - 1 to t
            #   add the ele to res lst
            # t += 1
        
        # return res lst

        left, top = 0, 0
        rows = len(matrix)
        cols = len(matrix[0])
        right = len(matrix[0])
        bottom = len(matrix)

        res = []

        while left < right and top < bottom:

            for c in range(left, right): # top row
                res.append(matrix[top][c])
            top += 1

            for r in range(top, bottom): # right row
                res.append(matrix[r][right - 1])
            right -= 1

            if top >= bottom or left >= right:
                break

            for c in range(right - 1, left - 1, -1): # bottom row
                res.append(matrix[bottom - 1][c])
            bottom -= 1

            for r in range(bottom - 1, top -1, -1): # left row
                res.append(matrix[r][left])
            left += 1

        return res






