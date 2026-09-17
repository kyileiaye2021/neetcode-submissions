class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # backtracking
        # backtrack func
        # base case
        # if the curr cell is out of bound or curr cell ele != word char or if cell is already visited:
        #   return false
        # visit the curr cell
        # call the backtrack func on the neighbors
        # unvisit the curr cell 
        
        # iterate thru every cell
        #   check if the curr cell is not visited
        #       call backtrack on the curr cell
        # return res

        res = False
        visited = set()
        ROWS = len(board)
        COLS = len(board[0])

        def dfs(r, c, i):
            if i == len(word):
                return True

            if r not in range(ROWS) or c not in range(COLS) or board[r][c] != word[i] or (r,c) in visited:
                return False

            visited.add((r, c))

            # go to 4 neighbors
            res = dfs(r + 1, c, i+1) or dfs(r-1, c, i+1) or dfs(r, c+1, i+1) or dfs(r, c-1, i+1) 

            visited.remove((r,c))
            
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c, 0):
                    return True

        return res




