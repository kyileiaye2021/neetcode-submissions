# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: 

    # subroot = None, and root = [1,2,3,4,5]  --> true
    
    # base case
    #   if root is none, subroot is not
    #       return false
    #   if subroot is none and root is not
    #       return true

    # if the root val == subroot val
    #   go to left and right subtree

    
    # dfs
    def sameTree(self, root, subRoot):
        if not root and not subRoot:
            return True

        if not root and subRoot:
            return False

        if root and not subRoot:
            return False

        if root.val != subRoot.val:
            return False
        
        return self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right)

    # 
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        
        if not root:
            return False

        if self.sameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

       

        