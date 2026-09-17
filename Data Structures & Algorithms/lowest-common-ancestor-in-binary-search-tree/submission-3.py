# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root, p, q):
        if p.val > root.val and q.val > root.val:
            return self.dfs(root.right, p, q)

        elif p.val < root.val and q.val < root.val:
            return self.dfs(root.left, p, q)

        elif p.val > root.val and q.val < root.val:
            return root

        elif p.val == root.val or q.val == root.val:
            return root
        return root

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # if p and q are none
        #   return cur node
        # both p and q > cur node
        #   find in the right subtree
        # both p and q < cur node
        #   find in the left subtree
        # if one is less than the curr node and the another is greater than the curr node
        #   return curr node
        # if == curr node
        #   return curr node
        return self.dfs(root, p, q)

