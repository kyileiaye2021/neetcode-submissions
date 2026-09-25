# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def recur_invert(root):
            if not root:
                return None

            root.left, root.right = root.right, root.left
            root.left = recur_invert(root.left)
            root.right = recur_invert(root.right)
            return root

        return recur_invert(root)
