# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # happy case
        # root : 1
        #       /  \
        #       2  3
        # output: [[1], [2, 3]]

        # edge case
        # root: [1]
        # output: [[1]]

        # root: []
        # output: []

        # bfs
        # queue
        # create a res list
        # append the first root node 
        # until the queue is empty
        # create a curr list
        # keep track of the len of queue each level
        # iterate that amount of queue len
        #   pop out the ele 
        #   add the popped ele to the curr list
        #   add the children of popped ele if they exist
        # append the curr list to the res list
        # return res list

        queue = deque([root])
        res = []

        if not root:
            return res

        while queue:
            curr_list = []
            queue_len = len(queue)

            for _ in range(queue_len):
                curr_node = queue.popleft()
                curr_list.append(curr_node.val)

                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
            
            res.append(curr_list)
        return res

