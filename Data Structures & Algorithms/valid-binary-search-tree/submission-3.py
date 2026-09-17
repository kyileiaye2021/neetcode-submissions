# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self,root, min_val, max_val):
        # if the root is none
        #   return true

        # if the root.val is out of min_val and max_val
        #   return false

        # go to left subttree with max val of curr root node val
        # go to right subtree with the min val of curr root node val
        # return true if both left and right tree returns true
        if not root:
            return True

        if root.val >= max_val or root.val <= min_val:
            return False

        left = self.dfs(root.left, min_val, root.val)
        right = self.dfs(root.right, root.val, max_val)
        return left and right
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
       # keep track of the max val for the left subtree
       # keep track of the min val for the right subtree
       # if the root is empty return true
       return self.dfs(root, float('-inf'), float('inf'))
