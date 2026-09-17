# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def sameTree(self, root, subroot):
        if not root and not subroot:
            return True

        if not root or not subroot:
            return False

        if root.val != subroot.val:
            return False

        return self.sameTree(root.left, subroot.left) and self.sameTree(root.right, subroot.right)

    def subRoot(self, root, subroot):
        # base case
        if not root and not subroot:
            return True

        if not root and subroot:
            return False

        if root and not subroot:
            return True

        if root.val == subroot.val:
            if self.sameTree(root, subroot):
                return True

        return self.subRoot(root.left, subroot) or self.subRoot(root.right, subroot)

    def isSubtree(self, root: Optional[TreeNode], subroot: Optional[TreeNode]) -> bool:

        return self.subRoot(root, subroot)
        