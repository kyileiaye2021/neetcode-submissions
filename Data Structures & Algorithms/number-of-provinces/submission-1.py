class Solution:
    def dfs(self, isConnected, i):
        isConnected[i][i] = 0
        for j in range(len(isConnected)):
            if isConnected[i][j] == 1:
                isConnected[i][j] = 0
                isConnected[j][i] = 0
                self.dfs(isConnected, j)
        
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        provinces = 0

        for i in range(n):
            if isConnected[i][i] == 1:
                self.dfs(isConnected, i)
                provinces += 1

        return provinces

    