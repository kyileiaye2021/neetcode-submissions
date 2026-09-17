class Solution:
    def dfs(self, r, c, grid, visited):
        # if the curr cell is water or out of range
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == 0:
            return 1

        if (r, c) in visited:
            return 0
        
        visited.add((r, c)) # mark the curr cell as visited
        perim = self.dfs(r + 1, c, grid, visited)
        perim += self.dfs(r - 1, c, grid, visited)
        perim += self.dfs(r, c + 1, grid, visited)
        perim += self.dfs(r, c - 1, grid, visited)
        return perim

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()
        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                        return self.dfs(r, c, grid, visited)

                