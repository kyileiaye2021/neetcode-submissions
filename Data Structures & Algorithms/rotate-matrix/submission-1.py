class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        # iterate thru the first row
        # after iterating trhu the first row
        #   the outer most cicle is done
        # update the pointers to go to inner ones

        # reverse the circle as we don't wanna keep a lot of variables

        # l, r 
        # 0, len(matrix[0]) - 1

        # iterate thru the matrix from l to r - 1 (excluding the last ele)
        #   top and bottom pointers
        #   keep track of top left
        #   assign bottom left ele to top left
        #   assign bottom right ele to bottom left
        #   assign top right ele to bottom right
        #   assign top left ele to top right
        # move l by 1 and move r by 1

        l, r = 0, len(matrix) - 1

        while l < r:
            for i in range(r - l):
                top = l
                bottom = r

                topleft = matrix[top][l + i]

                # assign bottom left to top left
                matrix[top][l + i] = matrix[bottom - i][l]

                # assign bottom right to bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # assign top right to bottom right
                matrix[bottom][r - i] = matrix[top + i][r] 

                matrix[top + i][r] = topleft

            l += 1
            r -= 1

        


        