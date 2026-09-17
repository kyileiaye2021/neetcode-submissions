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
        # create a dummy node
        # traverse the node in the linked list
        #   create a node with orig node val
        #   

        oldTonew_nodes = {None : None}

        # traverse the list to map old nodees to new nodes
        curr = head
        while curr:
            copy = Node(curr.val)
            oldTonew_nodes[curr] = copy
            curr = curr.next

        curr = head
        while curr:
            copy = oldTonew_nodes[curr]
            copy.next = oldTonew_nodes[curr.next]
            copy.random = oldTonew_nodes[curr.random]
            curr = curr.next

        return oldTonew_nodes[head]