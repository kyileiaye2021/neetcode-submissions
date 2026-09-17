class Solution:
    def dfs(self, r, c, board):
        if r not in range(len(board)) or c not in range(len(board[0])) or board[r][c] != 'O':
            return 
        
        board[r][c] = 'T'
        self.dfs(r + 1, c, board)
        self.dfs(r - 1, c, board)
        self.dfs(r, c + 1, board)
        self.dfs(r, c - 1, board)

    def solve(self, board: List[List[str]]) -> None:
        '''

        Input: board = [
        ["X","X","X","X"],
        ["X","O","O","X"],
        ["X","O","O","X"],
        ["X","X","X","O"]
        ]

        Output: [
        ["X","X","X","X"],
        ["X","X","X","X"],
        ["X","X","X","X"],
        ["X","X","X","O"]
        ]

        Input: board = [
        ["X","X","X","0"],
        ["X","O","O","X"],
        ["0","O","O","X"],
        ["X","X","X","O"]
        ]

        Output: [
        ["X","X","X","0"],
        ["X","O","O","X"],
        ["0","O","O","X"],
        ["X","X","X","O"]
        ]
        '''

        # dfs
        # unsurrounded regions 
        # convert them to the T
        
        # surrounded regions
        # convert O to X
        
        # convert them back to O

        rows = len(board)
        cols = len(board[0])

        for r in range(rows):
            for c in range(cols):
                if r in [0, rows - 1] or c in [0, cols - 1]:
                    if board[r][c] == "O":
                        self.dfs(r, c, board)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = 'X'

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    board[r][c] = "O"

        

        
