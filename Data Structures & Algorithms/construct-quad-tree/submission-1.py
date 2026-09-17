"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def helper(self, grid, n, r, c):
        allsame = True

        for i in range(n):
            for j in range(n):
                if grid[r][c] != grid[r + i][c + j]:
                    allsame = False
                    break

        if allsame:
            return Node(grid[r][c], True) # for leaf nodes

        n = n // 2
        topLeft = self.helper(grid, n, r, c)
        topRight = self.helper(grid, n, r, c + n)
        bottomLeft = self.helper(grid, n, r + n, c)
        bottomRight = self.helper(grid, n, r + n, c + n)
        return Node(0, False, topLeft, topRight, bottomLeft, bottomRight)

        
    def construct(self, grid: List[List[int]]) -> 'Node':
        # helper func
        # if all cells are equal, it is a leaf --> base case

        # divide the curr grid into four sub grids (need to change n)
        # find topleft, topRight, bottomLeft, bottomRight
        n = len(grid)
        r, c = 0, 0
        return self.helper(grid, n, r, c)

        
