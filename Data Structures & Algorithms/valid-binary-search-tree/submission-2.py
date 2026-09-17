# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # root = [2,1,3] -> true

    # root = none --> true
    # root = [2] --> true

    # if root == none
    #   return true

    # if the root val not within min max val
    #   return false

    # go to left subtree
    # go to right subtree
    def isValid(self, root, min_val, max_val):
        if not root:
            return True
        
        if root.val >= max_val or root.val <= min_val:
            return False

        return (self.isValid(root.left, min_val, root.val) and self.isValid(root.right, root.val, max_val))

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # set min max val for the root
        min_val = float('-inf')
        max_val = float('inf')

        return self.isValid(root, min_val, max_val)