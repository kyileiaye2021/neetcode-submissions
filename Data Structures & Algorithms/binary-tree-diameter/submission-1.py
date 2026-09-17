# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self, root, diameter):
        if not root:
            return 0

        left = self.helper(root.left, diameter)
        right = self.helper(root.right, diameter)
        diameter[0] = max(diameter[0], (left + right))
        return 1 + max(left, right)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
       # base case
       # if the tree is none or has only one node
       #    return 0
       # get left and right subtree
       # combine those to get diameter
       # return 1 + max(left &  right)
       diameter = [0]
       tree_height = self.helper(root, diameter)
       return diameter[0]
