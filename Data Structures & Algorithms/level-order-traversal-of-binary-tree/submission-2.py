# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #bfs
        queue = deque()
        queue.append(root)
        res_lst = []

        if not root:
            return res_lst

        while queue:
            
            queue_len = len(queue)
            curr_lst = []

            for _ in range(queue_len):
                curr_node = queue.popleft()
                print(curr_node.val)
                curr_lst.append(curr_node.val)

                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)

            res_lst.append(curr_lst)

        return res_lst



        