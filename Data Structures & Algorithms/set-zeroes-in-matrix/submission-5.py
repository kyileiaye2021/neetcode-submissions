class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        # set to store the row 
        # set to store the col
        
        # r_set = set()
        # c_set = set()

        # rows = len(matrix)
        # cols = len(matrix[0])

        # for r in range(rows):
        #     for c in range(cols):
        #         if matrix[r][c] == 0:
        #             r_set.add(r)
        #             c_set.add(c)


        # for r in r_set:
        #     for c in range(cols):
        #         matrix[r][c] = 0

        # for c in c_set:
        #     for r in range(rows):
        #         matrix[r][c] = 0
        # # time - O(m * n)
        # # space - O(m) + O(n)

        rows = len(matrix)
        cols = len(matrix[0])
        first_row = False

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0

                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        first_row = True

        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
            
        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0

        if first_row:
            for c in range(cols):
                matrix[0][c] = 0


                


                    
        
        