class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # change the 0s on the border cells to another char
        # change the surrounded 0s to X
        # change the converted chars to 0

        def dfs(x, y, coord):
            board[x][y] = '%'

            for dx, dy in coord:
                new_x, new_y = dx + x, dy + y
                if 0 <= new_x < len(board) and 0 <= new_y < len(board[0]) and board[new_x][new_y] == 'O':
                    dfs(new_x, new_y, coord)


        coord = [(1,0), (-1, 0), (0, 1), (0, -1)]
        for j in range(len(board[0])):
            if board[0][j] == 'O':
                dfs(0, j, coord)

            if board[len(board) - 1][j] == 'O':
                dfs(len(board) - 1, j, coord)

        for i in range(len(board)):
            if board[i][0] == 'O':
                dfs(i, 0, coord)

            if board[i][len(board[0]) - 1] == 'O':
                dfs(i, len(board[0]) - 1, coord)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '%':
                    board[i][j] = 'O'
