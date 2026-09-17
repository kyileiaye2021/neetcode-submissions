# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # happy cases
        #tree 1:1           
        #      / \
        #     2.  3
        #tree2: 1
        #      / \
        #     2.  3 
        # output: true

        #tree1: 1
        #      / \
        #     2.  3
        #tree2: 1
        #      / \
        #     2.  3
        #           \ 
        #            5
        # output: false

        # edge case:
        # input: tree1: none, tree2: none
        # output: true

        # input: tree1: 5, tree2: none
        # output: false

        # input: tree1: none, tree2: 9
        # output: false

        # input: tree1: 5, tree2: 6
        # output: false

        # DFS: 
        # base case
        # if both roots are none:
        # return true

        # if p root is none but q isn't 
        #   return false
        # if q root is none but p isn't
        #   return false

        # check if the p value and q value are not same
        #   return false

        # recursive call on the left sub tree and right subtrees of p and q trees

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
            left = self.isSameTree(p.left, q.left)
            right = self.isSameTree(p.right, q.right)
            return left and right
