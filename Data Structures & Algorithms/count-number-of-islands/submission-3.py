class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # dfs
        # visited()
        # dfs(x, y, coord)
        #   if x < len(grid) and y < len(grid[0]) and (x,y) not in visited
        #       visited.add((x, y))
        #   for (i, j) in coord:
        #       new_x = x + i
        #       new_y = y + j
        #       if new_x < len(grid) and new_y < len(grid[0]) and new_x and y not in visited:
        #           call dfs(new_x, new_y, coord)
        #
        # coord = [(1,0), (0,1), (-1, 0), (0, -1)]
        # iterate thru each cell
        #   if cell == '1' and not in visited yet
        #       dfs()
        #       count +=1
        # return count

        def dfs(x, y, coord, visited):
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and (x, y) not in visited:
                visited.add((x, y))
        
            for i, j in coord:
                new_x = x + i
                new_y = y + j

                if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and (new_x, new_y) not in visited and grid[new_x][new_y] == '1':
                    dfs(new_x, new_y, coord, visited)


        coord = [(1,0), (0,1), (0,-1), (-1, 0)]
        count = 0
        visited = set()
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == '1' and (x, y) not in visited:
                    dfs(x, y, coord, visited)
                    count += 1

        return count