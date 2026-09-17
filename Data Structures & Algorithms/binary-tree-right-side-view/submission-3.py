# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        # bfs
        res_lst = []
        if not root:
            return res_lst

        queue = deque()
        queue.append(root)

        while queue:

            queue_len = len(queue)
            right_node = queue[-1].val
            res_lst.append(right_node)

            for _ in range(queue_len):
                curr_node = queue.popleft()

                if curr_node.left:
                    queue.append(curr_node.left)

                if curr_node.right:
                    queue.append(curr_node.right)

        return res_lst

            
        