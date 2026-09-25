# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        is_balanced = True

        def recur_balanced(root):
            nonlocal is_balanced

            # base case
            if not root:
                return 0

            left = recur_balanced(root.left)
            right = recur_balanced(root.right)
            if abs(left - right) > 1:
                is_balanced = False

            return 1 + max(left, right)

        recur_balanced(root)
        return is_balanced