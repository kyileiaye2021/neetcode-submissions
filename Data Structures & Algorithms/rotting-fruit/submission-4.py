class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # bfs

        # dq 
        # num of fresh in grid
        # add the rotten oranges first and time = 0
        # while dq
        # rotten coord, time = dq.pop
        # go thru the nei
        #   if nei is within bound and if nei fresh
        #       add the nei coord with time + 1 into dq
        #       decrement fresh
        # return true if fresh == 0

        dq = collections.deque()
        fresh = 0
        coord = [(0,1), (0,-1), (1, 0), (-1, 0)]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh += 1

                if grid[i][j] == 2:
                    dq.append((i, j, 0))

        res_time = 0
        while dq:
            x, y, time = dq.popleft()
            res_time = time

            for dx, dy in coord:
                new_x, new_y = dx + x, dy + y

                if 0 <= new_x <len(grid) and 0<=new_y<len(grid[0]) and grid[new_x][new_y] == 1:
                    grid[new_x][new_y] = 2
                    fresh -= 1
                    dq.append((new_x, new_y, time + 1))
            
        return -1 if fresh > 0 else res_time



            
        