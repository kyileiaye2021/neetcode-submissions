class Solution:
    def dfs(self, i, par, visited, adj_lst):
        # base case
        if i in visited:
            return False

        visited.add(i)
        for nei in adj_lst[i]:
            if nei == par:
                continue

            if not self.dfs(nei, i, visited, adj_lst):
                return False
        return True

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_lst = {i: [] for i in range(n)}
        visited = set()
        for i, j in edges:
            adj_lst[i].append(j)
            adj_lst[j].append(i)

        res = self.dfs(0, -1, visited, adj_lst) 
        
        return res if len(visited) == n else False

        # num of nodes
        # child node cannot have 2 parents
        # dfs
        # graph {0 : [1,2,3], 1: [0,4], 2:[0], 3:[0], 4:[1]}
        # iterate thru the edges
        #   add the (i, j) pair to the graph
        #   add i as key and j as the list of value of i
        #   add j as key and i as the llist of values of j

        # visited set
        # queue
        # add the 0 to queue along parent (none)
        # until queue
        #   pop out the node
        #   go to the neighbors
        #   for each neighbor
        #       check if it's visited
        #           it's not parent node
        #               return false
        #           else: continue
        #       else:
        #           add the neighbor to the queue
        # return true

        # graph = defaultdict(list)
        # num_edges = 0

        # for x, y in edges:
        #     graph[x].append(y)
        #     graph[y].append(x)
        #     num_edges += 1

        # visited = set()
        # queue = deque()
        # queue.append((0, None))
        # visited.add(0)

        # while queue:
        #     curr_node, parent = queue.popleft()

        #     for child in graph[curr_node]:
        #         if child in visited:
        #             if child != parent:
        #                 return False
        #             else:
        #                 continue
        #         else:
        #             queue.append((child, curr_node))
        #             visited.add(child)

        # return True if n - num_edges == 1 else False



