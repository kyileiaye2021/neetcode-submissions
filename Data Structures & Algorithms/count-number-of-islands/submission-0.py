class Solution:
    # find the num of islands
        # happy cases
        # input: [
            #   [1, 0, 0],
            #   [1, 1, 0],
            #   [0, 0, 0]]
        # output: 1

        # edge cases
        # input: [[]]
        # output: 0

        # input: [[1]]
        # output: 1

        # input: [[0]]
        # output: 0
        
        # bfs
        # queue
        # add curr entry in the queue
        # mark that entry as visited
        # directions: [1,0], [-1,0], [0,1], [0,-1]
        # for each direction
        #   check if that entry is 1 and not visited
        #       add that entry to the queue and mark as visited

        # graph (BFS)
        # create a visited set
        # create a count var 
        # for every row in the grid
        #    for every col in the grid
        #       check if the curr entry is 1
        #           check if the curr is not visited 
        #               call bfs on the node and its neighbors
        #               increment count
    def bfs(self, grid, visited, r, c):
        queue = collections.deque()
        queue.append((r,c))
        visited.add((r,c))

        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        # go to the neighbors
        while queue:
            curr_r, curr_c = queue.popleft()

            for dir_r, dir_c in directions:
                new_r = curr_r + dir_r
                new_c = curr_c + dir_c

                # check if the new_r and new_c are in the bound of the grid
                if new_r in range(len(grid)) and new_c in range(len(grid[0])):
                    if grid[new_r][new_c] == '1' and (new_r, new_c) not in visited:
                        queue.append((new_r, new_c))
                        visited.add((new_r, new_c))

    def numIslands(self, grid: List[List[str]]) -> int:

        visited = set()
        island_count = 0

        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    self.bfs(grid, visited, r, c)
                    island_count += 1

        return island_count