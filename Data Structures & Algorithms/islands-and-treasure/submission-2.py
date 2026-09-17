class Solution:

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        # dfs (r ,c, dist)
        # marking that as visited
        # four neighbors for that cell
        # for each neighbor 
        #   check if the neighbor is within the bound and the neighbor is not -1 or not 0 
        #       check if dist < curr neighbor val
        #           update the curr neighbor val
        #   
        # iterate thru the cells in the grid
        # if the cell is 0
        #   if it is not visited
        #       call dfs on the cell

        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        queue = deque()
        dist = 0
        n = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c, dist))

        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while queue:
            curr_r, curr_c, curr_dist = queue.popleft()
            # print(f'curr_r: {curr_r}, curr_c: {curr_c}, curr dist: {curr_dist}')

            for dx, dy in dirs:

                new_r = curr_r + dx
                new_c = curr_c + dy
                new_dist = curr_dist + 1

                if new_r in range(rows) and new_c in range(cols) and grid[new_r][new_c] == 2147483647:
                    grid[new_r][new_c] = new_dist
                    queue.append((new_r, new_c, new_dist))