class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # iterate thru rows
        #   new set
        #   iterate thru cols
        #       if curr cell = '.': continue
        #       check if the curr ele in new set
        #           return false
        #       add the cur
      
        # iterate thru  cols
        #   new set
        #   iterate thru rows
        #      if curr cell = '.': continue
        #       check if the curr ele in new set
        #           return false
        #     

        # unique = {(r,c): set: [1 - 9]}
        # consider the group as a cell
        # 3 rows and 3 cols
        # iterate thru the rows
        #   iterate thru the cols
        #       if curr cell = '.':
        #           continue
        #       modified rc = (r/3, c/3)
        #       check if the ele is in the unique[(r/3, c/3)]
        #           return false
        #       add the curr ele to the dict unique

        rows = len(board)
        cols = len(board[0])

        for r in range(rows):
            temp = set()
            for c in range(cols):
                if board[r][c] == '.':
                    continue
                if board[r][c] in temp:
                    return False
                temp.add(board[r][c])

        for c in range(cols):
            temp = set()
            for r in range(rows):
                if board[r][c] == '.':
                    continue

                if board[r][c] in temp:
                    return False

                temp.add(board[r][c])

        unique = {} # {(r,c): set(1,2, ..)}
        for r in range(rows):
            for c in range(cols):
                if board[r][c] =='.':
                    continue
                
                modified_coord = (r // 3, c // 3)

                if modified_coord in unique:
                    if board[r][c] in unique[modified_coord]:
                        return False
                
                else:
                    unique[modified_coord] = set()

                unique[modified_coord].add(board[r][c])

        return True