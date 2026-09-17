# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root, balanced):
        # base case
        if not root:
            return 0

        left = self.dfs(root.left, balanced)
        right = self.dfs(root.right, balanced)

        diff = abs(left - right)
        if diff > 1:
            balanced[0] = False
        
        return 1 + max(left, right)

        
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = [True]
        self.dfs(root, balanced)
        return balanced[0]

        