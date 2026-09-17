# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # happy cases
        #       3
        #      / \
        #     2.  5
        #        / \
        #       4   6
        # output: 3

        # edge cases
        # input : None
        # output: None

        # input: 3
        # output: 3

        # 3
        #   \
        #    4
        #      \
        #       5
        # output: 3

        # find the maximum depth of the tree
        # DFS
        # base case
        # stop when the node is null 
        # update the len by increment by 1
        # call recursive on left and right subtree
        # return the max len of tree

        # base case
        if not root:
            return 0

        left_len = 1 + self.maxDepth(root.left)
        right_len = 1 + self.maxDepth(root.right)

        return max(left_len, right_len)

        

        