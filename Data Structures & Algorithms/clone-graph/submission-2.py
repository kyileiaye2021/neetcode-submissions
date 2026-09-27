"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # create a 2d array

        if not node:
            return None

        old_to_new = defaultdict(Node)


        # dfs 
        def dfs(n):
            if n in old_to_new:
                return old_to_new[n]
            new_node = Node(n.val)
            old_to_new[n] = new_node

            for nei in n.neighbors:
                new_node.neighbors.append(dfs(nei))

            return new_node

        return dfs(node)
            
        
