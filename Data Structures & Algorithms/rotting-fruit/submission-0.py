class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        # count all rotten fruit and add them to the queue
        # for each rotten fruit
        #   check if neighbors are within the range and fresh
        #       add them to the queue and marked as rotten
        #       decrement our fresh
        # increment time

        rows, cols = len(grid), len(grid[0])
        fresh = 0
        time_elapsed = 0

        queue = deque()
        directions = [[-1,0], [1,0], [0,1], [0,-1]]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))

                if grid[r][c] == 1:
                    fresh += 1

        while queue and fresh > 0:
            queue_len = len(queue)
            for _ in range(queue_len):

                curr_r, curr_c = queue.popleft()

                for dir_r, dir_c in directions:
                    new_r = dir_r + curr_r
                    new_c = dir_c + curr_c

                    if new_r in range(rows) and new_c in range(cols) and grid[new_r][new_c]==1:
                        queue.append((new_r, new_c))
                        fresh -= 1
                        grid[new_r][new_c] = 2

            time_elapsed += 1

        return time_elapsed if fresh == 0 else -1


        
                

