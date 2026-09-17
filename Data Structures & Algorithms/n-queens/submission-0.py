class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # backtracking
        
        # col set
        # posdiag set (r + c)
        # negdiag set (r - c)

        # res 
        # 2d chess board
        # dfs(r)
        # #base case
        # if r == n: 
        #   append chess board into the res
        # iterate thru the cols
        #   check if c is not in col set or r+ c not in posdiag or r - c not in negdiag
        #       put q to the curr cell
        #       put c to the col set
        #       put r + c to the posdiag
        #       put r - c to the negdiag
        #       call dfs on next row
        #       remove c from col set
        #       remove r + c from posdiag
        #       remove r - c from negdia
        #       put . to the curr cell

        # call dfs(0)
        # return res

        col = set()
        posdiag = set()
        negdiag = set()

        res = []

        board = [['.'] * n for i in range(n)]

        def dfs(r):
            # base case
            if r == n:
                copy = [''.join(row) for row in board]
                res.append(copy)
                return 

            for c in range(n):
                if c in col or (r + c) in posdiag or (r - c) in negdiag:
                    continue
                board[r][c] = 'Q'
                col.add(c)
                posdiag.add(r + c)
                negdiag.add(r - c)

                dfs(r + 1)

                board[r][c] = '.'
                col.remove(c)
                posdiag.remove(r + c)
                negdiag.remove(r - c)

        dfs(0)
        return res
