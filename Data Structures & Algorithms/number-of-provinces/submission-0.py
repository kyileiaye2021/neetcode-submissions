class Solution:
    def dfs(self, isConnected, i):
        for j in range(len(isConnected)):
            if isConnected[i][j] == 1:
                isConnected[i][j] = 0
                isConnected[j][i] = 0
                self.dfs(isConnected, j)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        provinces = 0

        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    provinces += 1
                    self.dfs(isConnected, i)


        return provinces

    