class Solution:
    def dfs(self,i, prev, visited, graph):
        if i in visited:
            return True
        
        visited.add(i)
        for neighbor in graph[i]:
            if neighbor == prev:
                continue
            if self.dfs(neighbor, i, visited, graph):
                return True
        
        return False

    def cycle_last_pair(self, edges):
        graph = collections.defaultdict(list)
        for (u, v) in edges:
            graph[u].append(v)
            graph[v].append(u)
            visited = set() # every time we create the new edge, we are checking the graph from scratch
            if self.dfs(u, -1, visited, graph):
                return [u, v]


    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # happy cases
        # input: edges = [[1, 2], [2,3], [1,3]]
        # output: [1,3]

        # input: edges = [[1, 2], [2,3], [1,3], [1,4]]
        # output: [1,3]

        # edge cases
        # input: edges = [[1, 2], [2,3], [1,3], [3,4], [4,5], [3,5]]
        # output: [3,5]

        # dfs 
        # base case: check if the curr i is visited: return 
        # mark the curr i as visited
        # for each neighbor
        #   check if neighbor is parent:
        #       continue
        #   append the pairs of curr i and neighbor to the route pairs
        #   call dfs on the neighbor

        # create a graph using the edges

        # visited set
        # traverse from 1 to n
        # route pairs 
        #   dfs on the curr i
        # check if the last 
        return self.cycle_last_pair(edges)
