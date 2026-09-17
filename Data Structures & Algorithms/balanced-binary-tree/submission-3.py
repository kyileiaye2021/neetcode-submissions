# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root, res):
        if not root:
            return 0
        
        left = self.dfs(root.left, res)
        right = self.dfs(root.right, res)

        if abs(left - right) > 1:
            res[0] = False

        return 1 + max(left, right)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = [True]
        tree_height = self.dfs(root, res)
        return res[0]


       