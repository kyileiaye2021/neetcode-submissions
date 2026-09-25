# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        # recur (root, p, q)
        # base case
        # if root == p or root == q
        # return root 
        # if root.val > both p and q val
        #   go to left subtree
        # if root.val < both p and q val
        #   go to right subtree

        #recur(root, p, q)

        def recur(root, p, q):
            if root.val == p or root.val == q:
                return root

            if root.val > p.val and root.val > q.val:
                return recur(root.left, p, q)

            elif root.val < p.val and root.val < q.val:
                return recur(root.right, p, q)

            else:
                return root
        return recur(root, p, q)

        