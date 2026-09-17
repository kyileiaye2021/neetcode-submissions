class Solution:
    def dfs(self, i, visited, graph):
        visited.add(i)

        for neighbor in graph[i]:
            if neighbor not in visited:
                self.dfs(neighbor, visited, graph)

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # happy cases
        # input: n = 3, edges = [[0,1], [0,2]]
        # output: 1

        # input: n = 6, edges = [[0, 1], [1, 2], [2,3], [4, 5]]
        # output: 2

        # edge cases
        # input: n = 0, edges = []
        # output: 0

        # input: n = 1, edges = []
        # output: 1

        # dfs 

        # dfs func 
        # mark the curr i as visited
        # for neighbors of each i
        #   call dfs func on each neighbor

    
        # create the graph 
        # create a map for the graph
        # iterate thru the edges 
        #   mapping the first ele to second ele
        #   mapping second ele to first ele

        # visited set 
        # count = 0
        # iterate from 0 to n -1  with i
        #   check if the curr i is already visited or not
        #       call dfs on cur i
        #       increment the count by 1

        # return count
        graph = collections.defaultdict(list)
        for (i, j) in edges:
            graph[i].append(j)
            graph[j].append(i)

        visited = set()
        count = 0

        for i in range(n):
            if i not in visited:
                self.dfs(i, visited, graph)
                count += 1
        
        return count
