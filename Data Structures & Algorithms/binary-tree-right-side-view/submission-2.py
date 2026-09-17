# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # happy case
        # root: [1, 2, 3]
        # output: [1, 3]

        # edge case
        # root: [1]
        # output: [1]

        # root: []
        # output: []

        # bfs
        # queue
        # num of nodes in each layer
        # do popleft 
        # if the popped node is the last node, add it to res list
        # add the children of the popped node

        queue = collections.deque([root])
        res = []

        if not root:
            return res

        while queue:
            curr_queue_len = len(queue)

            rightmost_node = queue[-1]
            res.append(rightmost_node.val)

            for _ in range(curr_queue_len):
                curr_node = queue.popleft()

                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)

        return res

            
