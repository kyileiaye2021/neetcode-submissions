# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        # base case
        # if not root:
        #   return False
        # if sameTree(root, subroot):
        #   return true
        # left = recursive call on left subtree
        # right = recursive call on right subtree
        # return left or right

        def recur_sameTree(root, subRoot):
            if not root and not subRoot:
                return True

            if not root or not subRoot:
                return False

            if root.val != subRoot.val:
                return False

            left = recur_sameTree(root.left, subRoot.left)
            right = recur_sameTree(root.right, subRoot.right)
            return left and right
    

        def recur_isSubtree(root, subRoot):
            if not root and not subRoot:
                return True

            if not root:
                return False

            if recur_sameTree(root, subRoot):
                return True

            left = recur_isSubtree(root.left, subRoot)
            right = recur_isSubtree(root.right, subRoot)
            return left or right

        return recur_isSubtree(root, subRoot)
            