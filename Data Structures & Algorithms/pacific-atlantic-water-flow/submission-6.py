class Solution:
        # add the curr (r, c) in the visted
        # iterate thru the neighbors
        #   check if the nei is in bound and nei height is greater than the curr height
        #       call dfs on the nei
    def dfs(self,r, c, visited, heights, directions):

        visited.add((r, c))

        for dx, dy in directions:
            new_r = r + dx
            new_c = c + dy

            if new_r in range(len(heights)) and new_c in range(len(heights[0])) and (new_r, new_c) not in visited and heights[new_r][new_c] >= heights[r][c]:
                self.dfs(new_r, new_c, visited, heights, directions)

        # store the cells that can flow to pacific 

        # store the cells that can flow to atlantic

        # if the nei cell height is larger than the curr cell
        #   go to the nei

        # iterate thru the first row and the last row
        #   if the cell is not visited (not in pacific set)
        #       call dfs on the cell

        # iterate thru the first and last col
        #   if the cell is not visited (not in atlantic )
        #       call dfs on the cell

        # find the common (r,c)s return the list

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        pac_set = set()
        atl_set = set()
        rows = len(heights)
        cols = len(heights[0])

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for c in range(cols): # pac
            if (0, c) not in pac_set:
                self.dfs(0, c, pac_set, heights, directions)
        
        for c in range(cols): # atl 
            if (rows - 1, c) not in atl_set:
                self.dfs(rows-1, c, atl_set, heights, directions)

        for r in range(rows): # pac
            if (r, 0) not in pac_set:
                self.dfs(r, 0, pac_set, heights, directions)

        for r in range(rows): # atl
            if (r, cols - 1) not in atl_set:
                self.dfs(r, cols - 1, atl_set, heights, directions)

        res = []
        for r, c in pac_set:
            if (r, c) in atl_set:
                res.append([r, c])
        
        return res


        