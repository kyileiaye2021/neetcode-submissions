# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # bfs
        # dq
        # add root into dq first
        # while dq
        #   len of curr dq
        #   add the last node of the res
        #   iterate thru dq len    
        #       pop the curr node
        #       if curr node. left
        #           add left to the q
        #       if curr node. right
        #           add right to q

        res = []
        if not root:
            return res

        dq = collections.deque()
        dq.append(root)

        while dq:
            length = len(dq)
            res.append(dq[-1].val)

            for _ in range(length):
                curr_node = dq.popleft()

                if curr_node.left:
                    dq.append(curr_node.left)

                if curr_node.right:
                    dq.append(curr_node.right)
                
        return res

        