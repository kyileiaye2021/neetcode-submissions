# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
   
    def helper(self, root):
        if not root:
            return 0

        left = self.helper(root.left)
        right = self.helper(root.right)
        return 1 + max(left, right)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # base case
        # if the root becomes null
        #   return 0
        # left subtree
        # right subree
        # get the max of left and right subtree
        # add 1 to the max value
        # return that num

        return self.helper(root)