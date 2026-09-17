# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def depth(self, root):
        # if root becomes none, return 0
        # left and right
        # count the num 
        # return max (left and right)
        if not root:
            return 0

        left = 1 + self.depth(root.left)
        right = 1 + self.depth(root.right)
        return max(left, right)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if the root is none: return 0
        # else:
        # left = recursive func 
        # right = recursive func 
        # return max(left, right) + 1
        depth = self.depth(root)
        return depth


        