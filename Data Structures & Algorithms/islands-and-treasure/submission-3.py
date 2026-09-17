class Solution:

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        # bfs 
        # queue
        # iterate thru the rows
        #   iterate thru the cols
        #       if curr cell is 0
        #           add the curr cell to queue with dist of 0
        # until queue is empty
        #   pop out the curr cell and dist
        #   go to the 4 neighbors
        #       check if the neighbor is within the bound and the curr neigbor is inf
        #           update the neighbor curr cell with the dist + 1
        #           add the neigbor to the queue with updated dist
        
        queue = deque()

        ROWS = len(grid)
        COLS = len(grid[0])
        dist = 0
        directions = [[0,1], [0,-1], [1,0], [-1,0]]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r,c,dist))

        while queue:
            curr_r, curr_c, curr_dist = queue.popleft()

            new_dist = curr_dist + 1
            for dir_r, dir_c in directions:
                new_r = curr_r + dir_r
                new_c = curr_c + dir_c

                if new_r in range(ROWS) and new_c in range(COLS) and grid[new_r][new_c] == 2147483647:
                    grid[new_r][new_c] = new_dist
                    queue.append((new_r, new_c, new_dist))

        


            