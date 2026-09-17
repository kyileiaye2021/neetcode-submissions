class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # bfs
        # queue
        # fresh
        # iterate thru the grid
        #   increment fresh if the cell is 1
        #   add the rotten fruit to the queue along with the time elapse (0)
        #   
        # untilt the queue is empty
        #   pop out the queue
        #   new time = time + 1
        #   go to the 4 directions
        #   check if the neighbor is within the bound and is 1:
        #       decrement fresh by 1
        #       add the neighbor to the queue along with the new time
        
        # if fresh = 0, return time

        queue = deque()
        fresh = 0
        time = 0

        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                
                if grid[r][c] == 2:
                    queue.append((r, c, time))

        while queue:
            curr_r, curr_c, curr_time = queue.popleft()
            time = curr_time

            for dx, dy in directions:
                new_r = curr_r + dx
                new_c = curr_c + dy
                new_time = curr_time + 1

                if new_r in range(rows) and new_c in range(cols) and grid[new_r][new_c] == 1:
                    fresh -= 1
                    grid[new_r][new_c] = 2
                    queue.append((new_r, new_c, new_time))

        if fresh == 0:  
            return time

        else:
            return -1
            


