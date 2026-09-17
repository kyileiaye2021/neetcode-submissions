class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # adj_list
        # indegree of size (n + 1)
        adj_lst = {i: [] for i in range(len(edges) + 1)}
        in_deg = [0] * (len(edges) + 1)

        for i, j in edges:
            adj_lst[i].append(j)
            adj_lst[j].append(i)
            in_deg[i] += 1
            in_deg[j] += 1
        
        queue = deque()
        
        for i in range(len(in_deg)):
            if in_deg[i] == 1:
                queue.append(i)

        while queue:
            cur_node = queue.popleft()
            in_deg[cur_node] -= 1

            for nei in adj_lst[cur_node]:
                in_deg[nei] -= 1
                if in_deg[nei] == 1:
                    queue.append(nei)

        for i, j in reversed(edges):
            if in_deg[i] == 2 and in_deg[j]:
                return [i, j]

        return []
        # queue 
        # excluding the node that are not part of the graph

        # iterate trhu the edges from the last 
        #   find the last edge