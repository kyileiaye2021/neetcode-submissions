# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # happy cases
        # root: 1
        #      / \
        #     2.  3
        # output: [1,3]

        # root: 3
        #      / \
        #     1.  4
        #       \
        #        2
        # output: [1,3,4]

        # edge cases
        # root: none
        # output: []

        # root: [2]
        # output: [2]

        # BFS 
        # queue to store the nodes in each level
        # res list to store rightmost node vals

        # iterate until queue is empty
        #   count the num of nodes in the queue
        #   iterate that amount of count 
        #       pop out the node from the right
        #       append the right node to the res list
        #       check if that node has children, append them to queue from left
        # return res list

        queue = deque()
        queue.append(root)
        added = False
        res_lst = []

        if not root:
            return res_lst
            
        while queue:
            count = len(queue)

            for _ in range(count):

                curr_node = queue.pop()
                if not added:
                    res_lst.append(curr_node.val)
                    added = True

                if curr_node.right:
                    queue.appendleft(curr_node.right)
                if curr_node.left:
                    queue.appendleft(curr_node.left)

            added = False

        return res_lst


        