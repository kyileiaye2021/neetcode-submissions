class NumMatrix:
    
    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self.newMatrix = [[0] * (cols + 1) for r in range(rows + 1)]

        for r in range(rows):
            prefix = 0
            for c in range(cols):
                prefix += matrix[r][c]
                above = self.newMatrix[r][c+ 1]
                self.newMatrix[r + 1][c + 1] = prefix + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # returning an integer
        row1, row2, col1, col2 = row1 + 1, row2 + 1, col1 + 1, col2 + 1
        rightBottom = self.newMatrix[row2][col2]
        above = self.newMatrix[row1-1][col2]
        left = self.newMatrix[row2][col1-1]
        topleft = self.newMatrix[row1-1][col1-1]
        return ((rightBottom - above) - (left - topleft))

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)