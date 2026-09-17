# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
     # edge cases
        # root: 1
        # return true

        # DFS 
        # base case: if node is none: return true
        # recursive call on left subtree
        # check if the curr node val is less than the prev node's val
        #   return false
        # recursive call on right subtree
        # both subtree should return true
    def isBST_helper(self, root, prev):
        if not root:
            return True
        
        # left
        left = self.isBST_helper(root.left, prev)
        
        #current
        if root.val <= prev[0]:
            return False

        # update the prev
        prev[0] = root.val

        # right
        right = self.isBST_helper(root.right, prev)

        return (left and right)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = [float('-inf')]
        return self.isBST_helper(root, prev)

    