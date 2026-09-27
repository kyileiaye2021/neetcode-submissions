class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        parent = [i for i in range(len(edges) + 1)] # initially each node is the parent of itself
        

        def find(node):
            if node != parent[node]:
                parent[node] = find(parent[node])

            return parent[node]

        def union(node1, node2):
            p1 = find(node1)
            p2 = find(node2)
            if p1 == p2:
                return False

            # if root parent of 2 nodes are in different components, merge them
            parent[p1] = p2
            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]
        
        