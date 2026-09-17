# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # happy cases
        #       3
        #      / \
        #.    2.  5
        #           \
        #            6
        # true

        #       6
        #      / \
        #     5.  8
        # true

        #       6
        #      / \
        #     2.  8
        #       \
        #        4
        #       / \
        #      3.  5
        # false

        # edge cases
        # input: empty
        # output: true

        # input: 3
        # output: true

        #       3
        #      /
        #     1
        # output: true

        # base case
        # if root is none, return true

        # input:  4
        # output: true

        # find the height of left subtree and right subtree
        # check if the difference is greater than 1, return false
        # otherwise, return true

    def isBalanced_helper(self, root, isbalanced):
        if not root:
            return 0
        
        left_subtree = self.isBalanced_helper(root.left, isbalanced)
        right_subtree = self.isBalanced_helper(root.right, isbalanced)

        # isbalanced[0] = abs(left_subtree - right_subtree) <= 1 # this can reset to True even after False in the steps
        isbalanced[0] = (isbalanced[0] and abs(left_subtree - right_subtree) <= 1)

        return 1 + max(left_subtree, right_subtree)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isbalanced = [True]
        self.isBalanced_helper(root, isbalanced)
        return isbalanced[0]


        
