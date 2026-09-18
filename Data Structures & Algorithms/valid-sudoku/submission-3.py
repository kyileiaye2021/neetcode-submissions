class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # hashmap {(x,y): [1,2,...]}
        # row map {row_num: [1,2,3,..]}
        # col map {col_num: [1,2,3,...]}

        # iterate thru the rows i
        #   iterate thru the col j
        #       check if the curr [i][j] is not .
        #           check if it is already in the row map
        #               return False
        #           add the curr ele to i key set

        #           check if it is already in the col map
        #               return False
        #           add the curr ele to j key set

        #       check if curr [i][j]  in (i/3, j/3)
        #           return False
        #       add curr [i][j] to the set of (i/3, j/3)

        # return True

        row_map = defaultdict(set)
        col_map = defaultdict(set)
        group_map = defaultdict(set)

        for i in range(9):
            for j in range(9):

                if board[i][j] != '.':

                    if board[i][j] in row_map[i]:
                        return False
                    elif board[i][j] in col_map[j]:
                        return False
                    elif board[i][j] in group_map[(i//3, j//3)]:
                        return False

                    else:
                        row_map[i].add(board[i][j])
                        col_map[j].add(board[i][j])
                        group_map[(i//3, j//3)].add(board[i][j])

        return True


