# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        # diameter = 0

        # recur(root)
        # nonlocal diameter
        # base case
        # if not root
        #   return 0

        # left = recur(root.left)
        # right = recur(root.right)
        # diameter = max(diameter, left + right)
        # return 1 + max(left, right)

        # recur(root)

        diameter = 0
        def recur(root):
            nonlocal diameter

            if not root:
                return 0

            left = recur(root.left)
            right = recur(root.right)
            diameter = max(diameter, left + right)
            return 1 + max(left, right)

        recur(root)
        return diameter

