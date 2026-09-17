class Solution:

    def bfs(self, n, queue, adj_lst, visited):
        # until the queue is empty
        #   pop out the curr node
        #   go to the neighbors
        #       check if the nei is not already visited
        #          add it to the queue and visited set
        queue.append(n)
        visited.add(n)
        while queue:
            curr_n = queue.popleft()

            for nei in adj_lst[curr_n]:
                if nei not in visited:
                    queue.append(nei)
                    visited.add(nei)


    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        # bfs
        # queue
        # visited set
        # iterate thru 0 - n - 1
        #   check if the curr node is not visited
        #       add the cur node to the queue
        #       add it to the visited set
        #       call bfs on the queue
        #       increment the count

        # return count
        adj_lst = {i: [] for i in range(n)}
        for i, j in edges:
            adj_lst[i].append(j)
            adj_lst[j].append(i)

        queue = deque()
        visited = set()
        count = 0

        for i in range(n):
            if i not in visited:
                self.bfs(i, queue, adj_lst, visited)
                count += 1

        return count
        