"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def clone_dfs(self, node, oldToNew):
        # if the node is already clone, return that clone node
        if node in oldToNew:
            return oldToNew[node] # we have to return the cloned node here

        # clone the node if it's not
        copy = Node(node.val)
        oldToNew[node] = copy

        # for each neighbor, we also need to clone
        for nei in node.neighbors:
            copy.neighbors.append(self.clone_dfs(nei, oldToNew))
        return copy


    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # happy cases
        # input: [[2], [1,3], [2]]
        # output: [[2], [1,3], [2]]

        # input: [[3],[1]]
        # output: [[3], [1]]

        # edge cases
        # input: [[]]
        # output: [[]]

        # input: [[], []]
        # output: [[], []]

        # input: []
        # output: []

        # dfs
        # hashmap to connect old to new node
        # dfs func
        # if the node is already in the map:
        #   return the node
        # check if the node is not in the map
        #   clone the node
        #   for the neighbor
        #       call dfs on the node

        oldToNew = {}
        if not node:
            return None
        else: 
            return self.clone_dfs(node, oldToNew)

