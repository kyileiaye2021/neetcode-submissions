class Solution:
    def createGraph(self, edges):
        graph = collections.defaultdict(list)
        for (i, j) in edges:
            graph[i].append(j)
            graph[j].append(i)
        return graph

    def dfs(self, i, prev, visited, graph):
        if i in visited:
            return False

        visited.add(i)
        for neighbor in graph[i]:
            if neighbor == prev: # to make sure there are no some false positives
                continue
            if not self.dfs(neighbor, i, visited, graph):
                return False

        return True

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # happy cases
        # input: n = 2
        # edges = [[0,1]]
        # output: true

        # input: n = 5
        # edges: [[0,1], [0,2], [2,3], [1,4]]
        # output: true

        # input: n =3
        # edges: [[0, 1], [1,2], [2, 0]]
        # output: false

        # edge cases
        # input: n = 1
        # edges: []
        # output: true

        # input: n = 4
        # edges: [[0, 1], [2, 3]]
        # output: true

        # dfs
        # dfs func
        #   if the curr num is already visited,return false
        #   mark the curr num as visited
        #   go to the neighbors 
        #       call dfs on the neighbor
        #   return true

        # visited set
        # create the graph with the edges {0: [1,2,3]
        #                                   1: [0,4], 2:[0], 3:[0]}
        # iterate thru the nums
        #   check if the curr num is not visited
        #   call dfs on the num

        visited = set()
        graph = self.createGraph(edges)

        return self.dfs(0, None, visited, graph) and n == len(visited)




