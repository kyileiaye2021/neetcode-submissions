class Solution:
    def waterflow_dfs(self, heights, r, c, visited, prevHeight):
        # check if the curr cell is already visited or it is out of the range of grid
        # or it's less than its prev height -> return
        # else: 
        #   mark the curr cell as visited in both pac and atl
        #   go to the 4 neighbors and call dfs on them
        if (r, c) in visited or r < 0 or c < 0 or r >= len(heights) or c >= len(heights[0]) or heights[r][c] < prevHeight:
            return

        visited.add((r, c))
        print((r,c))
        self.waterflow_dfs(heights, r + 1, c, visited, heights[r][c])
        self.waterflow_dfs(heights, r - 1, c, visited, heights[r][c])
        self.waterflow_dfs(heights, r, c + 1, visited, heights[r][c])
        self.waterflow_dfs(heights, r, c - 1, visited, heights[r][c])


    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # we are starting from the corners
        # we are iterating thru the first row and last row
        #   check if which cells can flow from ocean to inner parts
        # iterating thru the first col and last col
        #   check if which cells can flow from ocean to inner parts

        # ** water flows to equal or greater cell from the oceans!

        # have num of rows and cols
        # have visited set for each ocean (pac, atl)
        rows = len(heights)
        cols = len(heights[0])

        pac, atl = set(), set()

        # iterate thru the num of cols
        #   call dfs on first row col and last row col
        for c in range(cols):
            print('for each column')
            self.waterflow_dfs(heights, 0, c, pac, heights[0][c])
            self.waterflow_dfs(heights, rows - 1, c, atl, heights[rows - 1][c])

        # iterate thru the num of rows
        #   call dfs on first col row and last col row
        for r in range(rows):
            self.waterflow_dfs(heights, r, 0, pac, heights[r][0])
            self.waterflow_dfs(heights, r, cols-1, atl, heights[r][cols - 1])

        # iterate thru each row
        #   iterate thru each col
        #       if the curr cell in both pac and atl set
        #           add it to the res list

        res = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r, c])

        return res
        