class Solution:
    # def dfs(self, grid, r, count):
    #     grid[r][c] = 0
    #     count[0] += 1

    #     directions = [[1,0],[-1,0], [0,1], [0,-1]]

    #     for dir_r, dir_c in directions:
    #         new_r, new_c = r + dir_r, c + dir_c

    #         if new_r in range(len(grid)) and new_c in range(len(grid[0])) and grid[new_r][new_c] == 1:
    #             self.dfs(grid, new_r, new_c, count)

    def bfs(self, grid, r, c):
        queue = collections.deque()
        queue.append((r,c))
        grid[r][c] = 0

        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        count = 1
        # go to the neighbors
        while queue:
            curr_r, curr_c = queue.popleft()
            for dir_r, dir_c in directions:
                new_r = curr_r + dir_r
                new_c = curr_c + dir_c

                # check if the new_r and new_c are in the bound of the grid
                if new_r in range(len(grid)) and new_c in range(len(grid[0])):
                    if grid[new_r][new_c] == 1:
                        queue.append((new_r, new_c))
                        grid[new_r][new_c] = 0
                        count += 1
        return count

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # happy cases
        # input: grid = [[0,1,1,0,1],
        #                [1,0,1,0,1],
        #                [0,1,1,0,1],
        #                 0,1,0,0,1]]
        # output = 6

        # input: grid = [[0,1,0,0,1],
        #                [1,0,1,0,1],
        #                [0,1,1,0,1],
        #                [0,1,0,0,1]]
        # output = 4

        # input: grid = [[0,1,1,0,1],
        #                [1,0,0,0,0],
        #                [0,1,1,0,1],
        #                [0,1,0,0,0]]
        # output = 3
        
        # edge cases
        # input: grid = [[0,0,0,0,0],
        #                [0,0,0,0,0],
        #                [0,0,0,0,0],
        #                [0,0,0,0,0]]
        # output = 0

        # input: grid = [[1,1,1,1,1],
        #                [1,1,1,1,1],
        #                [1,1,1,1,1],
        #                [1,1,1,1,1]]
        # output = 20

        # input: grid = [[0,0,0,0,1],
        #                [0,0,0,1,0],
        #                [0,0,1,0,0],
        #                [0,1,0,0,0]]
        # output = 0 diagnoal thing


        # bfs

        # in dfs func
        #  mark the curr cell as visited
        #  directions - left, right, above, below
        #  for neighbor in directions
        #       if neighbor is within the boundary and it is 1
        #           go to the neighbor
        # 
        # check if the grid is empty, return 0     
        # create a visited to keep track of visited cells
        # create a max area 
        # iterate every row
        #   iterate every col
        #       check if the entry is visited
        #           call bfs and save the area
        #           update max area
        # return the max area

        if not grid:
            return 0

        max_area = 0

        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = self.bfs(grid, r, c)
                    max_area = max(max_area, area)

        return max_area



        