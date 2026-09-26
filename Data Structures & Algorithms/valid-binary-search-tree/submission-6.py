# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # post traversal
        # recur(root, lower, upper)
        # base case
        # if not root:
        #   return True

        # recursive case
        # if root.val <= lower or root.val >= upper:
        #   return False
        # left subtree(root.left, lower, root.val)
        # right subtree(root.right, root.val, upper)
        # return left and right

        # return recur(root, -inf, inf)
        
        def recur_BST(root, lower, upper):
            # base case
            if not root:
                return True

            # recursive case
            if root.val <= lower or root.val >= upper:
                return False

            return recur_BST(root.left, lower, root.val) and recur_BST(root.right, root.val, upper)

        return recur_BST(root, float('-inf'), float('inf'))
