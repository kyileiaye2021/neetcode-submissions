# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # happy case
        # input: [1, 2, 3, 4, 5, 6, 7]
        # output: [[1], [2,3], [4,5,6,7]]

        # edge case
        # input: []
        # output: []

        # input: [1]
        # output: [[1]]

        # input: [1, 2, null]
        # output: [[1], [2, null]]

        # BFS
        # queue to store the nodes in each level
        # res list to store the sublist of nodes in each level

        # iterate until queue is empty
        #   count the num of nodes in the queue
        #   iterate over that amount of times
        #       pop out the node from the left and append it to the list
        #       check if the curr node has children
        #           push them to the queue
        # return res list

        queue = deque()
        queue.append(root)
        res_lst = []

        if not root:
            return res_lst

        while queue:
            num = len(queue)
            level_lst = []

            for _ in range(num):
                curr_node = queue.popleft()
                level_lst.append(curr_node.val)

                if curr_node.left:
                    queue.append(curr_node.left)
                
                if curr_node.right:
                    queue.append(curr_node.right)

            res_lst.append(level_lst)

        return res_lst