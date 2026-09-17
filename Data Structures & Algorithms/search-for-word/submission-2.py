class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        directions = [[1, 0], [-1, 0], [0,1], [0,-1]]
        rows = len(board)
        cols = len(board[0])
        
        def dfs(i, r, c, visited):

            # need to check the char mismatch because at the last index the below case returns true right away
            if board[r][c] != word[i]:
                return False

            # base case
            if i == len(word) - 1:
                return True

            # mark the curr cell as visited
            visited.add((r,c))

            # go to nei
            for dx, dy in directions:
                new_r = r + dx
                new_c = c + dy

                if new_r in range(len(board)) and new_c in range(len(board[0])) and (new_r, new_c) not in visited:
                    if dfs(i + 1, new_r, new_c, visited):
                        return True

            visited.remove((r,c))
            return False

        visited = set()
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(0, r, c, visited):
                        return True

        return False
            

        
        # dfs  (# r, c, curr_path set, i)
        # base case
        # if i == len of word
        #   return true

        # if the curr cell is not the word[i] return false

            # mark the curr r, c as visited in curr path set

            # go to 4 neighbors
            #   check if the neighbor is within the bound and not visited in curr path set
            #       call dfs on the curr nei (with i + 1)


            # remove the curr r, c out of curr path set
        # return False