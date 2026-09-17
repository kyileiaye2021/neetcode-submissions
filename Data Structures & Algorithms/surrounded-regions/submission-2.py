class Solution:
    def bfs(self, r, c, grid):
        queue = collections.deque()
        queue.append((r,c))
        grid[r][c] = 'T'

        directions = [[1,0], [-1, 0], [0, 1], [0, -1]]

        while queue:
            curr_r, curr_c = queue.popleft()

            for dir_r, dir_c in directions:
                new_r = curr_r + dir_r
                new_c = curr_c + dir_c

                if new_r >= 0 and new_r < len(grid) and new_c >= 0 and new_c < len(grid[0]) and grid[new_r][new_c] == 'O':
                    grid[new_r][new_c] = 'T'
                    queue.append((new_r, new_c))


    def solve(self, board: List[List[str]]) -> None:
        # happy cases
        '''# input: [
            ["X","X","X","X"],
            ["X","O","O","X"],
            ["X","O","O","X"],
            ["X","X","X","O"]

        ]'''
        # output: 
        '''[
            ["X","X","X","X"],
            ["X","X","X","X"],
            ["X","X","X","X"],
            ["X","X","X","O"]
        ]
        '''

        # edge cases
        # input: none
        # output: none

        ''' ["X","O","O","X"],
            ["X","O","O","X"],
            ["X","X","X","X"],
            ["X","X","X","O"]
'''

        # BFS
        # queue
        # check if the curr r and curr c is greater than the first row and less than the last row and greater than the first col and less than the last col
        #   add the curr r, c  to queue
        # mark it as X
        # directions [left, right, above, and below]
        # for each directions
        #   check if new r and new c are within the boundary 
        #       mark the new cell as X

        # rows and cols
        # visited
        # for each row
        #   for each col
        #       check if the cell is a circle
        #           call bfs on the curr cell

        if not board:
            return None

        # For unsurrounded regions ('O' -> 'T')
        rows, cols = len(board), len(board[0])
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and (r in [0, (rows - 1)] or c in [0, (cols - 1)]):
                    self.bfs(r, c, board)

        # For surrounded regions ('O' -> 'X')
        for r in range (rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'

        # change unsurrounded regions 'T' back to 'O'
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'T':
                    board[r][c] = 'O'

