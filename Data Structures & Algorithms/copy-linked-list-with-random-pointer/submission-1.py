"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # oldToNew map
        oldToNew = {None: None}

        cur = head
        while cur:
            new_node = Node(cur.val)
            oldToNew[cur] = new_node
            cur = cur.next

        cur = head
        while cur:
            new_node = oldToNew[cur]
            new_node.next = oldToNew[cur.next]
            new_node.random = oldToNew[cur.random]
            cur = cur.next

        return oldToNew[head]

        
