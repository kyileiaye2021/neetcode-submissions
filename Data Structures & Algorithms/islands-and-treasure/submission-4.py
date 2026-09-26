class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # bfs
        # dq ((grid[x][y], dist))

        # iterate thru the cells
        #   if the cell == 0
        #       add those cells in dq

        # while dq
        #   curr val, curr dist = pop the curr cell 
        #   go thru nei cells
        #       if nei cell is within bound and is inf
        #           change the cell val to curr dist + 1
        #           add the cell to dq (nei cell, curr dist)
        
        dq = collections.deque()
        coord = [(0,1), (0, -1), (1, 0), (-1, 0)]

        for x in range(len(grid)):
            for y in range(len(grid[0])):

                if grid[x][y] == 0:
                    dq.append((x, y, 0))

        while dq:
            x, y, dist = dq.popleft()

            for dx, dy in coord:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] == 2147483647:
                    grid[new_x][new_y] = dist + 1
                    dq.append((new_x, new_y, dist + 1))

            





