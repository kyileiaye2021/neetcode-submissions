class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        # graph 
        # dfs
        # visited set
        # rows and cols
        # total = 0
        # iterate thru rows
        #   iterate thru cols
        #       check if the curr cell is not in visited 
        #           check if the curr cell is 1
        #               call dfs on that cell
        #               increment total by 1

        # dfs
        # base case
        # check if the curr cell is out of bound or not 1 or is already visited
        #   return
        #  make the curr cell as visitedd
        #  call dfs on neighbors

        ROWS =  len(grid)
        COLS = len(grid[0])
        visited = set()
        total = 0


        def dfs(r, c):
            # base case
            if r not in range(ROWS) or c not in range(COLS) or (r, c) in visited or grid[r][c]!= '1':
                return

            visited.add((r,c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visited and grid[r][c] == '1':
                    dfs(r,c)
                    total += 1

        return total
        