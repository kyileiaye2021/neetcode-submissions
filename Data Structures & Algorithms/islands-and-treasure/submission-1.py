class Solution:
       
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # bfs on the same multiple group
        # rows, cols
        # for each row
        #   for each col
        #       if curr cell is 0
        #           add them to the queue
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        dist = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))

        directions = [[0,1], [0,-1], [1, 0], [-1, 0]]

        while queue:
            queue_len = len(queue)
            dist += 1
            for _ in range(queue_len):
                curr_r, curr_c = queue.popleft()

                for dir_r, dir_c in directions:
                    new_r = dir_r + curr_r
                    new_c = dir_c + curr_c

                    if new_r in range(0, len(grid)) and new_c in range(0, len(grid[0])) and grid[new_r][new_c] == 2147483647: # if this is not visited
                        grid[new_r][new_c] = dist
                        queue.append((new_r, new_c))


                    