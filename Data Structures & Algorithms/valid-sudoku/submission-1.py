class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check if there are duplicates in the rows
        #   iterate thru the cols 9 times and check the duplicates

        # check if there are duplicates in the cols
        #   iterate thru the rows 9 times and check the duplicates

        # duplicates in the group
        r_set = defaultdict(set)
        c_set = defaultdict(set)
        group_set = defaultdict(set)
        for r in range(9):
            for c in range(9):
                
                if board[r][c] == '.':
                    continue 
                # if duplicates found, return false
                if board[r][c] in r_set[r] or board[r][c] in c_set[c] or board[r][c] in group_set[(r//3, c//3)]:
                    return False

                r_set[r].add(board[r][c])
                c_set[c].add(board[r][c])
                group_set[(r//3, c//3)].add(board[r][c])

        return True


                    


                
                
