"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def dfs(self, node, graph_map):

        # check if the node is already in the hashmap
        if node in graph_map:
            return graph_map[node]

        # create a new node of the original node
        new_node = Node(node.val)

        # add it to the hashmap
        graph_map[node] = new_node

        # go to the neighbor
        for nei in node.neighbors:
            new_node.neighbors.append(self.dfs(nei, graph_map))

        return new_node

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # store the val and its neighbors into a hashmap
        # {node: neighbors}\

        # create a hashmap for the nodes
        graph_map = {}
        return self.dfs(node, graph_map) if node else None


        

        # 