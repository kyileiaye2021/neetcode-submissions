class Solution:
    def dfs(self,r, c, visited, heights):
        visited.add((r, c))

        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for dx, dy in dirs:
            new_r, new_c = r + dx, c + dy
            if new_r in range(len(heights)) and new_c in range(len(heights[0])) and (new_r, new_c) not in visited and heights[new_r][new_c] >= heights[r][c]:
                self.dfs(new_r, new_c, visited, heights)


    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        # dfs 
        # mark the curr cell as visited
        # go to the neighbors
        # for each neighbor
        #   if the neighbor is greater than the curr cell
        #       call dfs on that neighbor

        # visited set
        # go from the row 0 and go from row -1
        # go from col 0 and go from col - 1

        # iterate thru the cols in the first row 
        #   check if the cells are not visited
        #       call dfs on that cell

        # iterate thru the cols in the last row
        #   check if the cells are not visited
        #       call dfs on that cell

        # iterate thru the rows in 1st col
        #   check if the cells are not viisted
        #       call dfs on that cell

        # iterate thru the rows in last col
        #   check if the cells are not visited
        #       call dfs on that cell

        pac = set()
        atn = set()
        res = []
        rows = len(heights)
        cols = len(heights[0])

        for c in range(cols):
            if heights[0][c] not in pac:
                self.dfs(0, c, pac, heights) # pacific
            if heights[rows-1][c] not in atn:
                self.dfs(rows - 1, c, atn, heights) # atlantic

        for r in range(rows):
            if heights[r][0] not in pac:
                self.dfs(r, 0, pac, heights) # pacific
            if heights[r][cols-1] not in atn:
                self.dfs(r, cols - 1, atn, heights) # atlantic

        print(pac)
        print(atn)
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atn:
                    res.append([r, c])
        return res





