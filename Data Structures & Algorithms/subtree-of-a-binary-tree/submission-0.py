# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Happy cases
        #  root:    1
        #          / \
        #         2.  3
        # subroot:  1
        #          / \
        #         2.  3
        # output: true

        # root:      1
        #          / \
        #         2.  3
        # subroot: 2
        # output: true

        # root:     1
        #          / \
        #         2.  3
        #               \
        #                5
        # subroot: 3
        #            \
        #             5
        # output: true
           
        # Edge cases:
        # root:     1
        #          / \
        #         2.  3
        # subroot: none
        # output: true

        # root: none
        # subroot: none
        # output: true

        # helper func (root, subroot, root_parent, subroot_parent)
        # base case 
        # both roots are none, return true
        
        # if root node exists and subroot node is none
        #   return true

        # if root node is none and subroot node is not
        #   return false

        # check if the root node val is = subroot val
        #   if subroot parent is not none
        #       check if parent root node is equal to subroot parent node
        #           call recursive call on the children of the root and subroot nodes
        #       else: return False
        #   else: 
        #       call recursive call on the children of the root and subroot nodes
        
        # else
        #   call recursive call on the children of the root but the subroot node is the same

        # return left and right

    def sameTree(self, p, q):
        # base case
        if not p and not q:
            return True

        if p and not q:
            return False
        
        if not p and q:
            return False

        if p.val != q.val:
            return False
        else:
            left = self.sameTree(p.left, q.left)
            right = self.sameTree(p.right, q.right)
            return left and right

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        # base case
        # order matters
        if not subRoot:
            return True
        if not root: 
            return False

        if self.sameTree(root, subRoot):
            return True

        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)

        return (left or right)
        