# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # recur(root):
        # base case
        # when root = none, return 0
        # return 1 + max(recur(root.left), recur(root.right))

        def recur(root):
            if not root:
                return 0

            return 1 + max(recur(root.left), recur(root.right))

        return recur(root)
        
        