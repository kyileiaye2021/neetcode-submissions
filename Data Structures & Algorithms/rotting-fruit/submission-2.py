class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        # bfs
        # minimum min = 0
        # create queue and min = 0
        # fresh = 0

        # iterate thru the matrix
        #   if the curr cell is 2
        #       add the curr cell to the queue with min. 0
        #   elif the curr cell == 1
        #       increment fresh

        # 4 dirs for each cell
        # until the queue is empty
        #   curr_r , curr_c, curr_min pop out the queue
        #   update minimum min

        #   go to the neighbors 
        #       if each neighbor is within bound and is 1
        #           decrement fresh
        #           replaace the curr neighbor cell with -2
        #           add those neighbor to the queue with min + 1

        # if fresh --> return - 1
        # else: return minimum min

        # min_minute = float('inf')
        curr_minute = 0
        queue = deque()
        fresh = 0

        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, curr_minute))

                elif grid[r][c] == 1:
                    fresh += 1

        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while queue:
            curr_r, curr_c, curr_min = queue.popleft()
            curr_minute = curr_min

            for dx, dy in dirs:
                new_r = curr_r + dx
                new_c = curr_c + dy
                new_min = curr_min + 1

                if new_r in range(rows) and new_c in range(cols) and grid[new_r][new_c] == 1:
                    grid[new_r][new_c] = 2
                    fresh -= 1
                    queue.append((new_r, new_c, new_min))

        return -1 if fresh > 0 else curr_minute


        