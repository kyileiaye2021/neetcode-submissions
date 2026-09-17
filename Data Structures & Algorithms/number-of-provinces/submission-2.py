class Solution:
    def dfs(self, visited, isConnected, i):
        visited[i] = True
        for j in range(len(isConnected)):
            if isConnected[i][j] == 1 and not visited[j]:
                self.dfs(visited, isConnected, j)
        
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        provinces = 0
        visited = [False] * n

        for i in range(n):
            if not visited[i]:
                self.dfs(visited, isConnected, i)
                provinces += 1

        return provinces

    