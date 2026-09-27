class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # border cells
        def dfs(x, y, visited, coord):
            if 0 <= x <len(heights) and 0 <= y < len(heights[0]) and (x,y) not in visited:
                visited.add((x, y))

                for dx, dy in coord:
                    new_x, new_y = x + dx, y + dy

                    if 0 <= new_x <len(heights) and 0 <= new_y < len(heights[0]) and (new_x,new_y) not in visited and heights[new_x][new_y] >= heights[x][y]:
                        dfs(new_x, new_y, visited, coord)

        coord = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        pacific = set()
        atlantic = set()
        for j in range(len(heights[0])):
            # pacific
            dfs(0, j, pacific, coord)
            # atlantic
            dfs(len(heights) - 1, j, atlantic, coord)

        for i in range(len(heights)):
            dfs(i, 0, pacific, coord)
            dfs(i, len(heights[0]) - 1, atlantic, coord)

        print(pacific)
        print(atlantic)
        res = []
        for x, y in pacific:
            if (x, y) in atlantic:
                res.append([x,y])

        return res