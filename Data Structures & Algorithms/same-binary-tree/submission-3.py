# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # happy cases
        # p = 1
        # q = 1
        # true

        # edge cases
        # p = None, q = None
        # true

        # p = [4] q = None
        # false

        # p = [None], q = [7]
        # false
        
        # base case
        # when p and q None
        #   return true

        # if not p and q
        #   return False

        # if not q and p
        #   return false

        # if p.val != q.val
        #    return false

        # left = recur(p.left, q.left)
        # right = recur(p.right, q.right)
        # return left and right

        def recur(p, q):
            if not p and not q:
                return True

            if not p and q:
                return False

            if not q and p:
                return False

            if p.val != q.val:
                return False

            left = recur(p.left, q.left)
            right = recur(p.right, q.right)
            return left and right

        return recur(p, q)
