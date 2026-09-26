class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        # dfs
        # dfs(x, y, coords):
        #   if x out of bound and y is out of bound or x, y == 0
        #       return 0
        #   convert curr cell to 0
        #   go thru nei cells
        #       res += call dfs (nei cells)
        # return 1 + res

        # max_area
        # iterate thru every cells
        # if cells is 1 and not visited
        #   count = dfs(x, y)
        #   max_area = max(count, max_area)
        # return max_area

        def dfs(x, y, coord):
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 0:
                return 0
            
            grid[x][y] = 0
            res = 0
            for i, j in coord:
                new_x, new_y = x + i, y + j
                res += dfs(new_x, new_y, coord)

            return 1 + res

        max_area = 0
        coord = [(1,0), (-1,0), (0, 1), (0, -1)]
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    count = dfs(x, y, coord)
                    max_area = max(max_area, count)

        return max_area
        