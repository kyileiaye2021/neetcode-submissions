class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # Check duplicates in 
        # each row 
        # each col
        # each square

        # Data structure for checking duplicates: set()
        # need to create hashmap because every row has same nums 
        # so need to know which row/col contains duplicates

        # hashmap for each row {row index: set()}
        # hashmap for each col {col index: set()}
        # set for each square {(row/3, col/3): set()} # need to divide by 3 to know which square the cell falls in

        row_set = collections.defaultdict(set)
        col_set = collections.defaultdict(set)
        square_set = collections.defaultdict(set)

        for i in range(9):

            for j in range(9):

                if board[i][j] == '.':
                    continue

                # if there is a duplicate in row, col, square
                if board[i][j] in row_set[i] or board[i][j] in col_set[j] or board[i][j] in square_set[(i // 3, j // 3)]:
                    return False

                else:
                    row_set[i].add(board[i][j])
                    col_set[j].add(board[i][j])
                    square_set[(i // 3, j // 3)].add(board[i][j])

        return True
