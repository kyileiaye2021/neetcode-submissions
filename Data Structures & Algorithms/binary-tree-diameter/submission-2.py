# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root, diameter):
        if not root:
            return 0

        left = self.dfs(root.left, diameter)
        right = self.dfs(root.right, diameter)

        diameter[0] = max(diameter[0], (left + right))
        return 1 + max(left, right)
    # dfs
    # if root becomes none
    #   return 0
    # left = call dfs
    # right = call dfs
    # diameter = max(diameter, left + right)
    # return 1 + max(left, right)


    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = [0]
        hei = self.dfs(root, diameter)
        return diameter[0]
        