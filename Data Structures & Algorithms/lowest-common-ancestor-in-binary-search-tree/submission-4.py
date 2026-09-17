# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root, p, q):
        if not p and not q:
            return root

        if not root:
            return None

        if p.val == root.val or q.val == root.val:
            return root
        elif p.val < root.val and q.val < root.val:
            return self.dfs(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.dfs(root.right, p, q)
        else:
            return root
        
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        return self.dfs(root, p, q)
        # p and q => none
        # root => none
        # return none

        # if p val or q val == root node val , return root node

        # if p and q vals < tree node
        #   p and q in left
        # elif p and q val > tree node
        #   p and q in right
        # else
        #   return root 